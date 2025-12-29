import requests
import random
import time
from datetime import datetime, timedelta

API_URL = "http://localhost:8000/predict"

def generate_random_payload():
    """Generate random store/item/date combinations."""
    random_days = random.randint(0, 365 * 2)  # within 2 years
    random_date = (datetime(2017, 1, 1) + timedelta(days=random_days)).strftime("%Y-%m-%d")

    return {
        "store": random.randint(1, 10),
        "item": random.randint(1, 50),
        "date": random_date
    }

def send_requests(n=200, delay_range=(0.5, 2.0)):
    """Continuously send prediction requests."""
    for i in range(n):
        payload = generate_random_payload()
        try:
            r = requests.post(API_URL, json=payload, timeout=5)
            print(f"{i+1:03} | Status: {r.status_code} | Payload: {payload} | Response: {r.json()}")
        except Exception as e:
            print(f"{i+1:03} | Error: {e}")
        time.sleep(random.uniform(*delay_range))

if __name__ == "__main__":
    send_requests(n=300)
