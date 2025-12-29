

## 🧩 **setup.md — Retail Demand Forecasting MLOps Pipeline**

### 📘 **Overview**

This document explains how to set up and run the **Retail Demand Forecasting MLOps Pipeline** — an end-to-end workflow that predicts product demand, detects model drift, retrains models, and redeploys automatically using free-tier tools.

---

## ⚙️ **1. Prerequisites**

Before setup, ensure you have:

| Requirement              | Version  | Purpose                 |
| ------------------------ | -------- | ----------------------- |
| **Python**               | ≥ 3.10   | Core development        |
| **Git**                  | latest   | Version control         |
| **Docker**               | latest   | Containerization        |
| **GitHub account**       | —        | CI/CD automation        |
| **DagsHub account**      | —        | DVC remote storage      |
| **Hugging Face account** | —        | API deployment (Spaces) |
| **Grafana & Prometheus** | optional | Monitoring stack        |

---

## 📦 **2. Project Structure**

 

```
retail-demand-forecasting-mlops/
│
├── .dvc/
│   ├── .gitignore            # Git ignore settings for DVC
│   └── config                # DVC configuration file
│
├── .github/
│   └── workflows/
│       └── retrain.yml       # GitHub Actions workflow for retraining
│
├── data/
│   ├── processed/
│   │   ├── .gitignore        # Git ignore settings for processed data
│   │   ├── cleaned_data.csv.dvc  # DVC-tracked cleaned data file
│   │   └── feature_data.csv  # Feature-engineered data
│   └── raw/
│       ├── sample_submission.csv  # Sample submission file
│       ├── test.csv              # Test dataset
│       └── train.csv             # Training dataset
│
├── logs/
│   ├── drift_logs.log         # Log for drift detection
│   └── retrain_logs.log       # Log for retraining pipeline
│
├── models/
│   ├── .gitignore             # Git ignore settings for models
│   ├── metrics.json           # Model evaluation metrics
│   └── model.pkl.dvc          # DVC-tracked model file
│
├── notebooks/
│   ├── 01_data_preparation.ipynb  # Notebook for data preparation
│   └── 02_drift_detection.ipynb   # Notebook for drift detection
│
├── reports/
│   ├── data_drift_report.html  # HTML report for data drift
│   └── drift_summary.json      # Summary of drift analysis
│
├── src/
│   ├── api/
│   │   ├── app.py             # FastAPI app for model serving
│   │   ├── predict.py         # Prediction logic for the API
│   │   └── utils.py           # Helper functions for model pulling
│   ├── drift/
│   │   └── drift_detection.py  # Drift detection logic
│   └── retraining/
│       ├── retrain_pipeline.py  # Retraining pipeline
│       └── test.py             # Unit tests for retraining pipeline
│
├── .dvcignore                 # Ignore file for DVC
├── .gitattributes             # Git attributes for handling files
├── .gitignore                 # Git ignore settings
├── Dockerfile                 # Dockerfile for containerization
├── LICENSE                    # Project license
├── README.md                  # Project documentation
├── docker-compose.yml         # Docker Compose setup
├── drift_result.txt           # Text file for drift results
├── dvc.yaml                   # DVC pipeline configuration
├── load_test.py               # Script for load testing
├── params.yaml                # Configuration parameters
├── prometheus.yml             # Prometheus configuration for monitoring
└── requirements.txt           # Project dependencies
```




---

## 🧱 **3. Environment Setup**

### 🧰 Step 3.1 — Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows
```

### 📦 Step 3.2 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧑‍💻 **4. Local Development Workflow**

### 🔹 Data Preparation

```bash
python src/data_prep.py
```

Cleans raw data, creates time-based and lag features, and stores processed data under `data/processed/`.

### 🔹 Model Training

```bash
python src/train_model.py
```

Trains the model, evaluates metrics (MAE, RMSE, MAPE), and saves it as `models/model_latest.pkl`.

### 🔹 Drift Detection

```bash
python src/drift_detection.py
```

Runs data & concept drift detection using **Evidently AI** and logs results to console or JSON.

---

## 🚀 **5. API Deployment (FastAPI)**

### 🧩 Step 5.1 — Run Locally

```bash
uvicorn src.api.app:app --reload
```

API available at → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
Test `/predict` endpoint with JSON input.

### 🐳 Step 5.2 — Docker Build

```bash
docker build -t retail-forecast-api .
docker run -p 8000:8000 retail-forecast-api
```

### ☁️ Step 5.3 — Deploy on Hugging Face Spaces

1. Create a new **Space** (Type: Docker).
2. Push repo to Hugging Face:

   ```bash
   git remote add space https://huggingface.co/spaces/<USERNAME>/<SPACE_NAME>
   git push space main
   ```
3. Hugging Face automatically builds and deploys your container.

---

## 📊 **6. Monitoring Setup (Prometheus + Grafana)**

### 🐳 Step 6.1 — Launch Monitoring Stack

```bash
docker-compose up --build
```

Access:

* **FastAPI** → [http://localhost:8000](http://localhost:8000)
* **Prometheus** → [http://localhost:9090](http://localhost:9090)
* **Grafana** → [http://localhost:3000](http://localhost:3000) (admin / admin)

### 🔍 Step 6.2 — Grafana Setup

* Add Prometheus as a data source (`http://prometheus:9090`)
* Create dashboards using metrics:

  * `request_count`
  * `prediction_count`
  * `request_latency_seconds`

---

## ⚙️ **7. CI/CD Automation (GitHub Actions)**

The pipeline is defined in `.github/workflows/retrain.yml`.

### Workflow Steps:

1. Pull latest data/model from DagsHub (DVC)
2. Retrain model automatically
3. Push updated model to DagsHub
4. Redeploy Hugging Face Space

### Required GitHub Secrets:

| Secret          | Description               |
| --------------- | ------------------------- |
| `DAGSHUB_TOKEN` | Access token from DagsHub |
| `DAGSHUB_USER`  | Your DagsHub username     |
| `HF_TOKEN`      | Hugging Face Access Token |
| `HF_USERNAME`   | Hugging Face username     |
| `HF_SPACE`      | Hugging Face Space name   |

---

## 🧾 **8. Reproducibility Checklist**

| Component        | Tool                         | Configured | Verified |
| ---------------- | ---------------------------- | ---------- | -------- |
| Data Versioning  | DVC + DagsHub                | ✅          | ✅        |
| Model Versioning | DVC                          | ✅          | ✅        |
| Drift Detection  | Evidently AI                 | ✅          | ✅        |
| CI/CD            | GitHub Actions               | ✅          | ✅        |
| Deployment       | FastAPI + Docker + HF Spaces | ✅          | ✅        |
| Monitoring       | Prometheus + Grafana         | ✅          | ✅        |

---

## 🧠 **9. Notes for Reproducibility**

* All scripts are deterministic with `random_state=42`.
* Each stage (data, model, drift, deployment) is modular and can be run independently.
* To reproduce a previous version, checkout the corresponding Git commit and use:

  ```bash
  dvc checkout
  ```
* All pipeline components use **only free-tier services**.

---

## 🏁 **10. Project Summary**

| Stage            | Tool                                   | Description                   |
| ---------------- | -------------------------------------- | ----------------------------- |
| Data Preparation | Pandas, Scikit-learn                   | Feature engineering           |
| Model Training   | XGBoost / RandomForest                 | Regression-based forecasting  |
| Drift Detection  | Evidently AI                           | Data + concept drift tracking |
| Retraining       | DVC + GitHub Actions                   | Automated on change           |
| Deployment       | FastAPI + Docker + Hugging Face Spaces | API serving                   |
| Monitoring       | Prometheus + Grafana                   | Metrics visualization         |

---

✅ **Setup complete!**
This `setup.md` ensures anyone can **replicate, run, and maintain** the retail demand forecasting MLOps pipeline, developed by **Shehab Hegab**.


