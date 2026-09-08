# StudioSync — Grant Application / Project Proposal

## 1. Applicant

**Name:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337

## 2. Project title

**StudioSync: An Agentic Operations Layer for Real-Time Film Production Recovery**

## 3. Executive summary

StudioSync is a production-operations intelligence system designed to reduce the coordination cost of film and media production disruptions. A single incident — a location cancellation, weather event, schedule shift or supplier constraint — can propagate across multiple operational domains. StudioSync converts that incident into a structured, auditable recovery workflow.

The prototype uses a multi-agent architecture built around Google Agent Development Kit (ADK) and Gemini models. A coordinator decomposes the incident into specialist investigations covering scenario impact, logistics recovery and financial risk. The financial specialist can be grounded in production analytics through the ClickHouse MCP integration. The coordinator then reconciles evidence, ranks recovery options and identifies decisions that require explicit human approval.

The project is intentionally positioned as operational software, not AI-generated cinema content. Its objective is to shorten the path from disruption to a defensible production decision while preserving traceability and human authority.

## 4. Problem and unmet need

Production teams operate across interconnected systems: schedules, scripts, locations, cast and crew availability, transport, equipment, procurement and cost tracking. When one assumption changes, the resulting impact is frequently reconciled manually.

This creates three structural problems:

- **Slow response:** decision-makers must gather and reconcile information across multiple sources.
- **Hidden dependency risk:** operational consequences can remain invisible until downstream work is already committed.
- **Weak auditability:** urgent decisions may be communicated through fragmented messages, spreadsheets and informal approvals.

The unmet need is therefore not another passive dashboard. It is an evidence-aware operational layer capable of coordinating multi-step analysis and presenting the resulting decision package to a human production lead.

## 5. Proposed solution

StudioSync introduces an explicit agentic control loop:

**Interpret → Decompose → Investigate → Ground → Reconcile → Recommend → Approve**

The system separates responsibilities among specialist agents rather than relying on a single monolithic prompt. This allows the application to preserve role-specific instructions, evidence boundaries and approval policies.

The initial workflow focuses on emergency recovery after a production disruption. Example input:

> “A storm cancels Scene 42. Find suitable alternatives, assess schedule and logistics impact, and calculate the budget delta.”

The resulting brief contains:

- incident interpretation;
- affected operational dependencies;
- ranked alternative locations;
- cost and schedule considerations;
- evidence provenance;
- confidence information;
- explicit human approval requirements.

## 6. Technical architecture

### 6.1 Application layer

A FastAPI service provides the public application surface and exposes health, integration-status and analysis endpoints. A responsive web cockpit presents the incident and the resulting decision package.

### 6.2 Agent layer

The configured runtime uses Google ADK and Gemini with a coordinator plus parallel specialist agents:

- **ScenarioImpactAgent** — models the operational consequences of the incident.
- **LocationLogisticsAgent** — evaluates recovery options.
- **FinancialRiskAgent** — performs financial analysis with tool grounding.
- **StudioSyncCoordinator** — reconciles findings and identifies the approval boundary.

### 6.3 Analytics grounding

ClickHouse serves as the analytical grounding layer in the configured path. The integration is exposed through MCP so the financial agent can access the approved analytical capability without embedding database-specific application logic into the agent itself.

The project follows a read-only-by-default principle. Credentials are runtime configuration and are not stored in source control.

### 6.4 Evidence model

The data contract distinguishes four evidence classes:

1. **user_input** — information directly supplied in the incident request;
2. **synthetic** — reproducible demonstration fixtures;
3. **mcp** — values retrieved through configured external tooling;
4. **model_inference** — conclusions or estimates produced by the model.

This distinction is essential for responsible operational AI because a recommendation should not make a synthetic fixture look like a live enterprise fact.

## 7. Prototype maturity

The public repository contains:

- application source code;
- multi-agent orchestration code;
- typed domain models;
- deterministic demo data;
- web interface;
- automated tests;
- CI configuration;
- Docker packaging;
- Cloud Run deployment guidance;
- architecture documentation;
- demonstration script;
- competition submission copy.

The prototype deliberately supports two modes:

**Demo mode** is deterministic and credential-free. It exists for reproducible evaluation.

**Live/configured mode** requires explicit Google Cloud and ClickHouse MCP configuration. The system does not silently fall back to synthetic data when a live execution is requested.

## 8. Innovation

StudioSync differentiates itself through the combination of:

**Agentic decomposition.** The system turns one operational request into parallel specialist work rather than producing a single free-form answer.

**Analytical grounding.** Financial reasoning can be connected to an external analytical system through MCP rather than relying solely on model memory.

**Evidence-aware outputs.** The result contract exposes where a conclusion came from.

**Approval-aware execution.** The model is positioned as a decision-support and orchestration layer; consequential production changes remain subject to human authorization.

**Production-specific framing.** The product is designed around a concrete workflow in film operations rather than a generic AI assistant.

## 9. Expected impact

The first impact target is operational response time. StudioSync should reduce the interval between an incident being reported and the delivery of a structured, reviewable recovery proposal.

Pilot evaluation will measure:

- median incident-to-plan time;
- number of manual reconciliation steps;
- number of systems or workstreams touched per incident;
- time to produce a budget delta;
- percentage of recommendations containing provenance;
- percentage of consequential actions blocked until explicit approval.

The project intentionally does **not** present unverified production savings as historical facts. Those savings should be established through controlled pilot measurement against the production team’s existing baseline.

## 10. Target users and market

Primary users are:

- production managers;
- line producers;
- production coordinators;
- studio operations teams;
- production-service companies;
- broadcasters and media organizations with complex scheduling operations.

The product is designed as an orchestration layer above existing systems. This reduces adoption friction because StudioSync can begin with imported or synthetic data and progressively connect to scheduling, procurement, finance and location systems.

## 11. Security and responsible AI

The prototype follows several principles:

- least-privilege access to external systems;
- read-only analytics by default;
- secrets supplied only through runtime configuration;
- explicit distinction between tool evidence and model inference;
- explicit human authorization for consequential actions;
- no claim of external execution without tool confirmation;
- deterministic demo data clearly labeled as synthetic.

Future productionization should add identity-aware access control, policy engines, comprehensive audit logs, tenant isolation and connector-specific permission boundaries.

## 12. Implementation plan

### Phase 1 — Prototype hardening

Validate representative incident datasets, strengthen automated evaluations, complete live ClickHouse MCP connectivity, measure latency and model/tool cost, and improve deployment observability.

### Phase 2 — Pilot validation

Run controlled pilots on a small set of real production workflows. Compare StudioSync against existing operating procedures and establish measurable improvements in response time, reconciliation effort and decision quality.

### Phase 3 — Productionization

Introduce identity-aware access, policy enforcement, enterprise audit logging, production connector management, data retention controls and multi-project deployment patterns.

### Phase 4 — Commercial expansion

Extend the platform into additional production workflows such as procurement variance detection, location replacement, schedule recovery, equipment substitution and cross-department incident coordination.

## 13. Funding use

Grant support will be used to convert the hackathon-grade prototype into a validated operational pilot. Priority uses are:

- evaluation and benchmark infrastructure;
- secure cloud runtime and observability;
- production-grade MCP integration;
- enterprise security controls;
- connector engineering;
- pilot deployment and measurement;
- documentation and commercialization preparation.

A final financial budget should be attached according to the specific grant programme requirements rather than invented from unsupported assumptions.

## 14. Risk management

**Model error:** constrained outputs, typed contracts, evidence provenance and human review reduce the effect of incorrect generation.

**Tool/data error:** integration failures are surfaced explicitly; live mode does not silently substitute demo data.

**Unauthorized action:** the initial architecture keeps consequential actions behind approval gates.

**Adoption friction:** StudioSync is designed as a layer above existing systems rather than a forced ERP replacement.

**Vendor dependency:** the architecture isolates agent orchestration from specific analytical backends through MCP, enabling future connector substitution.

## 15. Success definition

The project will be considered successful when a production team can submit a real operational disruption and receive, within a materially shorter time than its baseline process, a structured recovery plan whose key recommendations are traceable to data or clearly labeled as inference, with all consequential changes remaining under explicit human authority.

## 16. Applicant statement

I am proposing StudioSync as a practical application of agentic AI to a real operational problem in film production. The purpose is not to remove human production expertise. The purpose is to augment it with a coordinated, evidence-aware system that can investigate cascading consequences faster, make assumptions visible and help production leaders act with greater confidence under time pressure.

**Applicant:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337
