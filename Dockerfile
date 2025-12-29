# Use a lightweight base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code and requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose API port
EXPOSE 8000

# Command to run the API
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
