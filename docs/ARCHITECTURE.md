# StudioSync Architecture

## Product contract
StudioSync is a production-operations decision system, not a content-generation chatbot. A natural-language production incident is decomposed into three specialist analyses: scenario impact, location/logistics recovery, and financial risk. The coordinator reconciles the results into a ranked plan with explicit approval gates.

## Runtime graph
```text
User / Web UI
      |
      v
StudioSync Coordinator (Gemini via ADK)
      |
      v
Parallel Specialist Stage
  |        |        |
Scenario  Location  Financial
Impact    Logistics Risk
                    |
                    v
             ClickHouse MCP
             read-only analytics
      |        |        |
      +--------+--------+
               v
       Reconciled action brief
               |
         Human approval gate
```

The repository uses Google ADK agents and workflow primitives. ADK supports sequential and parallel multi-agent patterns; the project uses a parallel specialist stage so independent investigations can run concurrently.

## ClickHouse integration
The partner requirement is met only when the deployment points to the official ClickHouse MCP server through `CLICKHOUSE_MCP_URL`. The application requests only read-oriented analytics from that integration. The official ClickHouse MCP server exposes `run_query` and defaults to read-only operation; production deployments should also use authentication and a restricted database role.

## Safety
No external state-changing operation is claimed to occur automatically. The prototype exposes approval checkpoints instead. Query execution is bounded by environment policy and external MCP configuration; sensitive credentials belong in runtime secret management, never in Git.
