from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    hostname = os.environ.get("APP_NAME", "unknown")
    return {"message": f"Hello from {hostname}!"}