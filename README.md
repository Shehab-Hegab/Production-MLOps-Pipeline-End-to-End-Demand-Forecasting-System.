
# **Store Item Demand Forecasting – End-to-End MLOps Pipeline**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-lightgrey)
![DVC](https://img.shields.io/badge/DVC-Data%20Versioning-purple)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-yellow)
![License](https://img.shields.io/badge/License-MIT-blue)

## **Overview**

This project implements an **end-to-end MLOps pipeline** for forecasting daily sales of retail store items using machine learning.
The pipeline integrates data preprocessing, drift detection, automated retraining, version control, continuous integration and deployment (CI/CD), and monitoring — providing a complete, production-ready forecasting solution.

Key objectives include:

* Predicting daily store item sales using machine learning regression models.
* Monitoring data and concept drift to maintain model accuracy.
* Automating retraining and deployment through CI/CD pipelines.
* Exposing the latest model via a REST API built with FastAPI.
* Enabling live monitoring and alerting with Prometheus and Grafana.

---

## **Project Workflow**

Below is the high-level workflow of the project:

![Project Workflow](assets/workflow.png)

---

## **1. Data Preparation and Model Development**

The project begins with preparing the dataset, engineering predictive features, and developing a baseline regression model.

**Key tasks include:**

* Loading and cleaning the Kaggle sales dataset (`train.csv`), handling missing values and outliers.
* Engineering temporal features (`year`, `month`, `day`, `dayofweek`, `is_weekend`) and lag-based features (`lag_1`, `lag_7`, `lag_30`) with rolling statistics (`rolling_mean_7`, `rolling_mean_30`).
* Splitting the dataset chronologically into training and testing subsets.
* Training baseline regression models such as **XGBoostRegressor** and **RandomForestRegressor**.
* Evaluating model performance using **MAE**, **RMSE**, and **MAPE**.
* Saving the trained model (`models/model.pkl`) and corresponding metrics (`models/metrics.json`) for later use.

This forms the foundation of the forecasting pipeline, enabling consistent model benchmarking and evaluation.

---

## **2. Drift Detection and Model Monitoring**

To ensure long-term reliability, the pipeline incorporates mechanisms for detecting **data drift** and **concept drift**.

**Data Drift Detection:**

* Implemented using the **Evidently AI** library to compare feature distributions between reference (training) data and incoming data.
* Generated drift reports in HTML format summarizing detected changes.

**Concept Drift Detection:**

* Compared model performance on new data against baseline metrics.
* Triggered drift alerts if performance degradation exceeded defined thresholds (e.g., MAPE increase >20%).
* Logged drift results in `logs/drift_logs.log` and summarized outcomes in `reports/drift_summary.json`.

These capabilities ensure the system proactively identifies when retraining is required, maintaining forecasting accuracy over time.

---

## **3. Automated Retraining Pipeline**

Model retraining is fully automated through a reproducible and version-controlled workflow.

**Core components:**

* **Data and Model Versioning:**
  Implemented using **DVC (Data Version Control)** with **DagsHub** as the remote storage backend. This ensures versioned datasets and models are tracked efficiently outside the Git repository.

![DagsHub Integration](assets/dagshub_repo.png)

* **Retraining Script:**
  The retraining pipeline (`src/retraining/retrain_pipeline.py`) automatically:

  * Loads the latest data managed by DVC.
  * Performs consistent feature preparation.
  * Retrains the model using defined algorithms.
  * Evaluates the new model and updates versioned artifacts with timestamped identifiers.
  * Logs all retraining events for auditability.

* **Automated Triggering:**
  Drift detection generates a flag file signaling when retraining should occur. The retraining pipeline reads this flag and executes automatically.

* **GitHub Actions Integration:**
  A scheduled **GitHub Actions** workflow automates the entire retraining and update process — from detecting drift to committing new artifacts and pushing updates to DagsHub.

This design enables seamless, event-driven model updates without manual intervention.

---

## **4. Model Deployment via FastAPI and Docker**

The latest trained model is deployed as a REST API using **FastAPI**, providing real-time prediction capabilities.

**Deployment Architecture:**

* A FastAPI app (`src/api/app.py`) exposes endpoints:

  * `/` – API health check.
  * `/predict` – Accepts input features and returns sales forecasts.
* The API dynamically loads the latest model version using DVC integration with DagsHub.
* The application is containerized with **Docker**, ensuring environment consistency and portability.
* Deployment is hosted on **Hugging Face Spaces**, enabling public access and easy scalability.

This component transforms the trained forecasting model into a production-ready, cloud-deployed microservice.

---

## **5. Monitoring and Alerting**

A complete monitoring and alerting system is integrated to provide visibility into API performance and operational health.

![Grafana Dashboard](assets/grafana_dashboard.png)

**Stack Components:**

* **Prometheus:** Collects runtime metrics such as request count, latency, and error rates from the FastAPI `/metrics` endpoint.
* **Grafana:** Visualizes these metrics through customizable dashboards.
* **Prometheus Client (Python):** Used within the FastAPI app for instrumentation.
* **Docker Compose:** Orchestrates the FastAPI, Prometheus, and Grafana services into a unified monitoring stack.

![Prometheus Graph](assets/prometheus_graph.png)

Users can view:

* Request throughput and latency trends.
* Prediction volume and API uptime.
* Drift detection and retraining frequency metrics.

This setup ensures end-to-end observability and supports future extensions for automated alerting and notifications.

---

## **6. CI/CD Integration for Continuous Model Updates**

The project features a **fully automated CI/CD pipeline** that integrates model retraining, testing, and redeployment.

**Pipeline Workflow (via GitHub Actions):**

1. **Environment Setup** – Installs dependencies and synchronizes data/models from DVC/DagsHub.
2. **Drift Evaluation** – Analyzes drift reports to determine if retraining is necessary.
3. **Model Retraining** – Executes the retraining script to produce updated models and metrics.
4. **Artifact Versioning** – Saves and pushes updated artifacts to DagsHub via DVC.
5. **Container Rebuild & Deployment** – Rebuilds and redeploys the FastAPI Docker image to Hugging Face Spaces.
6. **Validation & Logging** – Tests the `/predict` endpoint, verifies metrics, and records retraining logs.

This CI/CD automation ensures the forecasting model remains continuously updated and deployable, aligning with modern MLOps best practices.

---

## **Architecture Summary**

The Store Item Demand Forecasting system integrates the following components:

| Layer               | Technology                           | Purpose                               |
| ------------------- | ------------------------------------ | ------------------------------------- |
| **Data Processing** | Pandas, NumPy, Scikit-learn          | Data cleaning, feature engineering    |
| **Modeling**        | XGBoost, RandomForest                | Forecasting daily item demand         |
| **Version Control** | DVC, DagsHub                         | Data and model versioning             |
| **Monitoring**      | Prometheus, Grafana                  | Real-time metric visualization        |
| **Deployment**      | FastAPI, Docker, Hugging Face Spaces | API serving                           |
| **Automation**      | GitHub Actions                       | CI/CD for retraining and redeployment |

---

## **Conclusion**

This project delivers a **comprehensive MLOps pipeline** for demand forecasting — spanning from data ingestion to deployment and continuous monitoring.

Through the integration of open-source technologies like **Evidently AI**, **DVC**, **FastAPI**, **Prometheus**, and **GitHub Actions**, the system achieves:

* Automated model lifecycle management.
* Continuous adaptation to changing data.
* Scalable, containerized deployment.
* Transparent monitoring and retraining workflows.

The result is a robust, production-grade architecture capable of maintaining high model reliability and operational efficiency in dynamic environments.

---

## 👨‍💻 **Author**

**Developed by [Shehab Hegab](https://github.com/Shehab-Hegab)**

Feel free to connect or reach out for collaborations!


