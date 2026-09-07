from core.models import *

def demo_result(instruction: str, configured: bool=False) -> StudioSyncResult:
    return StudioSyncResult(
        incident_summary="Storm-driven cancellation of Scene 42; StudioSync converts a disruption into a ranked recovery plan.",
        scenario_changes=[ScenarioChange(scene_id="42", change="Exterior shoot cancelled due to severe weather", operational_effects=["Move production into a controlled interior location", "Re-check crew and cast windows", "Recalculate overtime, location and transport costs"])],
        studio_options=[
            StudioOption(name="Studio B", available_window="Next 24h", fit_score=0.93, estimated_cost=18000, notes="Best operational fit; minimal set rebuild"),
            StudioOption(name="Warehouse 42", available_window="24–48h", fit_score=0.81, estimated_cost=12500, notes="Lower venue cost; higher art-department conversion effort"),
            StudioOption(name="Stage C", available_window="36–48h", fit_score=0.74, estimated_cost=21000, notes="Strong capacity; adds transport complexity"),
        ],
        budget=BudgetDelta(baseline=150000, revised=174000, delta=24000, confidence="medium"),
        approvals=Approval(status="required", actions=["Approve selected location", "Approve revised cost ceiling", "Approve any overtime or contractual change", "Release updated call sheet after approval"]),
        provenance=["Synthetic demonstration dataset embedded for reproducible judging", "Google ADK graph available in configured runtime", "ClickHouse MCP is used only when CLICKHOUSE_MCP_URL and credentials are configured"],
    )
