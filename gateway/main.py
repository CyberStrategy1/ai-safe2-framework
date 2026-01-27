from fastapi import FastAPI, Request, HTTPException
import yaml
import time
from prometheus_client import Counter, Histogram, generate_latest

app = FastAPI(title="AI SAFE² Gateway")

# Metrics
REQUEST_COUNT = Counter('requests_total', 'Total AI requests', ['status'])
LATENCY = Histogram('request_latency_seconds', 'Request latency')

# Load Config
try:
    with open("config/default.yaml", "r") as f:
        CONFIG = yaml.safe_load(f)
except FileNotFoundError:
    CONFIG = {}

@app.get("/health")
async def health_check():
    return {"status": "active", "version": "2.1.0"}

@app.middleware("http")
async def governance_middleware(request: Request, call_next):
    start_time = time.time()
    
    # 1. P3.T5.1: Rate Limiting (Redis check placeholder)
    # 2. P1.T1.2: Input Sanitization logic
    
    response = await call_next(request)
    
    # 3. P2.T3.1: Audit Logging
    REQUEST_COUNT.labels(status=response.status_code).inc()
    LATENCY.observe(time.time() - start_time)
    
    return response

@app.get("/metrics")
async def metrics():
    return generate_latest()

# Stub for LLM Proxy
@app.post("/v1/chat/completions")
async def proxy_chat():
    return {"message": "Gateway Enforcement Active"}
