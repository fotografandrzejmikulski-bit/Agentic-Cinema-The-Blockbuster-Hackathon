# StudioSync

**Agentic production recovery for film & media — Gemini + Google ADK + ClickHouse MCP**

StudioSync is an operational decision layer for film production teams. It converts a production disruption into a structured, auditable recovery brief: scenario impact, ranked location/logistics options, financial delta, provenance, and explicit human approval gates.

> This is intentionally **not** a video-generation demo. The product targets the operational work required to make a production happen.

## Why this fits Agentic Cinema

The official hackathon requires a functional Gemini/Google Cloud agent or multi-agent network using a partner product or MCP server at runtime, plus a hosted project, public open-source repository, and demo video. The ClickHouse track specifically requires active runtime use of the official `mcp-clickhouse` server. The project is therefore structured around a real agent graph and a real MCP integration path, while retaining a deterministic local demo so the product can be inspected without private credentials.

**Current hackathon deadline:** September 9, 2026 at 2:00 PM PDT. Judging uses four equally weighted criteria: Technological Implementation, Design, Potential Impact, and Quality of the Idea.

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
./scripts/run_local.sh
```

Open `http://127.0.0.1:8080`.

Run tests with `pytest -q`.

See `docs/ARCHITECTURE.md`, `docs/DEMO_SCRIPT.md`, `docs/DEVPOST_SUBMISSION.md`, and `docs/GRANT_APPLICATION.md` for the full technical and application package.

## License

Apache-2.0
