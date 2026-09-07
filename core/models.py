from pydantic import BaseModel, Field
from typing import Literal

class ScenarioChange(BaseModel):
    scene_id: str
    change: str
    operational_effects: list[str] = Field(default_factory=list)

class StudioOption(BaseModel):
    name: str
    available_window: str
    fit_score: float
    estimated_cost: float
    notes: str

class BudgetDelta(BaseModel):
    baseline: float
    revised: float
    delta: float
    currency: str = "USD"
    confidence: Literal["low","medium","high"] = "medium"

class Approval(BaseModel):
    status: Literal["required","not_required","approved"]
    actions: list[str] = Field(default_factory=list)

class StudioSyncResult(BaseModel):
    incident_summary: str
    scenario_changes: list[ScenarioChange]
    studio_options: list[StudioOption]
    budget: BudgetDelta
    approvals: Approval
    provenance: list[str]
