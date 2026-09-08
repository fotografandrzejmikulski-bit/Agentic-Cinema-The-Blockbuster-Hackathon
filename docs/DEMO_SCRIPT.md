# 3-Minute Demo Script

**Applicant:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337

## 0:00–0:20 — The operational problem

> “A storm cancels Scene 42. That single change can trigger location, cast, crew, transport, overtime and budget consequences. Production leadership needs a recovery plan, not another chatbot answer.”

## 0:20–0:45 — Natural-language incident

Enter:

> “A storm cancels Scene 42. Find the best recovery option within 48 hours and quantify the budget delta.”

Immediately point out the system mode indicator: **Demo** for the reproducible fixture or **Configured** for a deployed Gemini + ClickHouse MCP environment.

## 0:45–1:25 — Agentic decomposition

Show the coordinator and the three specialist roles:

- Scenario Impact Agent
- Location & Logistics Agent
- Financial Risk Agent

Explain that these are independent subproblems that can be investigated in parallel and reconciled by the coordinator.

For the configured run, show the financial path reaching ClickHouse through MCP. Do not claim a live query result unless the demo visibly proves it.

## 1:25–2:05 — Evidence-aware decision cockpit

Show:

- ranked studio alternatives;
- fit score and estimated cost;
- budget delta;
- confidence;
- evidence provenance.

Point out the distinction between synthetic fixture values, user input, model inference and MCP-retrieved evidence.

## 2:05–2:35 — Human approval gate

Show the approval requirements:

- approve the selected location;
- approve the revised cost ceiling;
- approve any overtime or contractual change;
- release the updated call sheet only after approval.

State clearly: the prototype does not silently mutate external systems.

## 2:35–3:00 — Closing statement

> “StudioSync is not a movie generator. It is an agentic operations layer for the people who have to make the production happen. It connects reasoning, analytics, evidence and human authority in one recovery loop.”
