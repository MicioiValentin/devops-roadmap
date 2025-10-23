import json
import logging
import time
from datetime import datetime, UTC
from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="hello-api")

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": datetime.fromtimestamp(record.created, UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            payload["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)

root = logging.getLogger()
root.setLevel(logging.INFO)
for h in list(root.handlers):
    root.removeHandler(h)
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
root.addHandler(handler)
log = logging.getLogger("app")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status"],
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency seconds",
    ["method", "path"],
    buckets=(0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2, 5),
)

@app.middleware("http")
async def metrics_and_logging(request: Request, call_next):
    start = time.perf_counter()
    response: Response = await call_next(request)
    dur = time.perf_counter() - start
    path = request.url.path
    REQUEST_LATENCY.labels(request.method, path).observe(dur)
    REQUEST_COUNT.labels(request.method, path, str(response.status_code)).inc()
    log.info(f"{request.method} {path} {response.status_code} {dur:.4f}s")
    return response

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/hello")
def hello(name: str = "Vali"):
    return {"message": f"Hello, {name}"}

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return PlainTextResponse(content=data.decode("utf-8"), media_type=CONTENT_TYPE_LATEST)
