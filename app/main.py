from __future__ import annotations

import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from agents.orchestrator import run_studiosync

app = FastAPI(title="StudioSync", version="1.0.0")


class AnalyzeRequest(BaseModel):
    instruction: str = Field(min_length=10, max_length=4000)
    mode: str = Field(default="demo", pattern="^(demo|live)$")


@app.get("/health")
def health():
    return {"status": "ok", "service": "studiosync", "version": app.version}


@app.get("/api/status")
def status():
    return {
        "service": "studiosync",
        "mode": os.getenv("STUDIOSYNC_MODE", "demo"),
        "gemini_configured": bool(os.getenv("GOOGLE_CLOUD_PROJECT")),
        "clickhouse_mcp_configured": bool(os.getenv("CLICKHOUSE_MCP_URL")),
        "safety": "human approval required for consequential actions",
    }


@app.get("/", response_class=HTMLResponse)
def index():
    with open("web/index.html", encoding="utf-8") as handle:
        return handle.read()


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    try:
        return run_studiosync(req.instruction, req.mode)
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
