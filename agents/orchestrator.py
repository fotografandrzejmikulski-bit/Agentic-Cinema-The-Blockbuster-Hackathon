import os
from typing import Any
try:
    from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
except Exception:
    LlmAgent = SequentialAgent = ParallelAgent = None

try:
    from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams
except Exception:
    McpToolset = None
    StreamableHTTPConnectionParams = None

from core.models import StudioSyncResult
from services.demo_data import demo_result

MODEL=os.getenv("GEMINI_MODEL","gemini-2.5-flash")

def _mcp_toolset():
    url=os.getenv("CLICKHOUSE_MCP_URL")
    token=os.getenv("CLICKHOUSE_MCP_AUTH_TOKEN")
    if not url or McpToolset is None:
        return None
    headers={"Accept":"application/json, text/event-stream"}
    if token:
        headers["Authorization"]=f"Bearer {token}"
    return McpToolset(connection_params=StreamableHTTPConnectionParams(url=url, headers=headers))

def build_agent_graph():
    if LlmAgent is None or ParallelAgent is None:
        raise RuntimeError("google-adk is not installed; install requirements.txt to enable the Gemini/ADK runtime graph")
    toolset=_mcp_toolset()
    financial_tools=[toolset] if toolset else []
    scenario_agent=LlmAgent(name="ScenarioImpactAgent", model=MODEL, instruction=(
        "Identify operational consequences of a film-script change. Return concise structured findings; never invent contractual facts."
    ))
    logistics_agent=LlmAgent(name="LocationLogisticsAgent", model=MODEL, instruction=(
        "Evaluate location alternatives for a production disruption. Rank options by fit, schedule feasibility and estimated cost."
    ))
    financial_agent=LlmAgent(name="FinancialRiskAgent", model=MODEL, tools=financial_tools, instruction=(
        "Quantify budget deltas. When ClickHouse MCP is configured, query the production analytics database using its read-only tools. "
        "Do not perform writes. Clearly distinguish retrieved values from estimates."
    ))
    parallel=ParallelAgent(name="ProductionAnalysisParallel", sub_agents=[scenario_agent, logistics_agent, financial_agent])
    coordinator=LlmAgent(name="StudioSyncCoordinator", model=MODEL, instruction=(
        "Act as the production operations lead. Decompose an incident into scenario, logistics and finance work; reconcile outputs; "
        "identify human approvals; and produce an auditable action brief. Never claim an external action was executed unless a tool confirms it."
    ), sub_agents=[parallel])
    return coordinator

def run_studiosync(instruction: str) -> dict[str, Any]:
    configured=bool(os.getenv("GOOGLE_CLOUD_PROJECT") and os.getenv("CLICKHOUSE_MCP_URL"))
    result=demo_result(instruction, configured=configured)
    return result.model_dump()
