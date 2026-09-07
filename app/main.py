from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from agents.orchestrator import run_studiosync

app = FastAPI(title="StudioSync", version="0.1.0")

class AnalyzeRequest(BaseModel):
    instruction: str

@app.get("/health")
def health():
    return {"status":"ok","service":"studiosync"}

@app.get("/", response_class=HTMLResponse)
def index():
    return open("web/index.html", encoding="utf-8").read()

@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    return run_studiosync(req.instruction)
