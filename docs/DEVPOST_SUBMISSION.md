# Devpost Submission Draft — ClickHouse Track

## Project
**StudioSync — Agentic Production Recovery**

## Applicant
**Andrzej Mikulski**  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337

## One-line pitch
**StudioSync turns production disruptions into evidence-aware recovery plans, grounding financial analysis in ClickHouse through MCP while keeping humans in control of consequential decisions.**

## The problem
A film-production disruption rarely affects one variable. A cancelled scene can cascade into location availability, crew calls, cast windows, transport, equipment, overtime exposure and budget burn. Conventional production software records these facts but leaves the cross-system reconciliation to people.

StudioSync targets that reconciliation gap.

## What the prototype does
A production lead submits an incident in natural language. StudioSync decomposes it into parallel specialist work:

1. **Scenario Impact Agent** — identifies operational consequences and dependencies.
2. **Location & Logistics Agent** — ranks recovery options by feasibility, fit and estimated cost.
3. **Financial Risk Agent** — grounds budget analysis in ClickHouse through the configured MCP integration.
4. **Coordinator** — reconciles the specialist outputs into one decision brief.
5. **Approval Gate** — makes consequential decisions explicit before any external state change.

## Why ClickHouse
ClickHouse is used as the analytical grounding layer for operational measurements such as cost events, schedule deltas and logistics metrics. MCP turns that analytical capability into an agent-accessible interface. The repository keeps the integration explicit through `CLICKHOUSE_MCP_URL` and does not claim live ClickHouse results in demo mode.

## Why this is agentic
This is not a chat wrapper around a single model. The core unit is a multi-stage decision loop: **interpret → decompose → investigate in parallel → ground in tools → reconcile → propose → require approval**.

The system is designed so that different specialists can operate independently and the coordinator remains responsible for the final synthesis. This is the key product behavior demonstrated by the prototype.

## Judging alignment

| Criterion | Evidence | What judges can verify |
|---|---|---|
| Technological Implementation | `agents/orchestrator.py`, `core/models.py`, `app/main.py` | ADK-based agent graph, typed result contract, MCP configuration and explicit live/demo separation |
| Design | `web/index.html` | Incident input, ranked recovery options, budget impact, provenance and approval visibility |
| Potential Impact | `docs/GRANT_APPLICATION.md` | Operational problem, pilot metrics and commercialization path |
| Quality of the Idea | Production-recovery workflow | Agentic reasoning is applied to a real operational bottleneck rather than content generation |

## Reproducibility
The repository provides deterministic demo mode so a reviewer can inspect the complete product contract without private credentials. A configured environment enables the Gemini/ADK graph and ClickHouse MCP integration path.

Critically, the application never silently converts a synthetic fixture into a claimed live database result.

## Responsible AI
StudioSync separates four evidence classes: user input, synthetic fixture data, tool-retrieved evidence and model inference. Financial analysis is read-only by default. The initial workflow requires explicit human authorization for consequential production changes.

## Demo scenario
The demonstration uses a storm-driven cancellation of Scene 42. The system produces alternative locations, estimated budget impact, evidence provenance, confidence and approval requirements. The result is intended to demonstrate decision quality and transparency, not to imply that the displayed synthetic values come from a live production database.

## Known limitation and next validation step
The public repository contains the complete integration path but cannot prove a live ClickHouse-backed execution without a configured endpoint and credentials. The next validation step is a hosted deployment using the official ClickHouse MCP server and a restricted read-only role, followed by a recorded end-to-end run.

## Repository
The repository is public, open source under Apache-2.0, and includes application code, tests, deployment guidance and submission documentation.
