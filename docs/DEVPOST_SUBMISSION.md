# Devpost Submission Draft — ClickHouse Track

## One-line pitch
**StudioSync turns production disruptions into a ranked recovery plan grounded in ClickHouse analytics — with humans in control of every consequential decision.**

## What it does
When a production disruption occurs, StudioSync decomposes the problem into parallel specialist analyses, grounds the financial layer in ClickHouse via MCP, and returns a coherent decision brief: what changed, which options are viable, what the budget impact is, and what requires approval.

## Why ClickHouse
ClickHouse is used as the analytical system-of-record for high-volume operational measurements such as cost events, schedule deltas and logistics metrics. The official `mcp-clickhouse` integration turns those analytics capabilities into agent-accessible tools at runtime.

## Judging alignment
| Criterion | Evidence in repository |
|---|---|
| Technological Implementation | Google ADK agent graph, Gemini model configuration, official ClickHouse MCP integration point, CI tests |
| Design | Responsive production-operations cockpit with incident input, ranked recovery options, budget delta and approval state |
| Potential Impact | Targets measurable time-to-decision, reconciliation effort and budget variance in a real workflow |
| Quality of Idea | Uses agentic reasoning as an operational control loop rather than a content-generation demo |

## Reproducibility
The repository includes a deterministic demo path that works without secrets, plus a configured path that uses Gemini and ClickHouse MCP. This is intentional: judges can inspect the software immediately and then enable cloud integrations when credentials are available.

## Limitations stated honestly
The repository cannot claim a live ClickHouse-backed run from source alone until `CLICKHOUSE_MCP_URL` and credentials are configured. No production savings are presented as established facts; pilot metrics are explicit targets.
