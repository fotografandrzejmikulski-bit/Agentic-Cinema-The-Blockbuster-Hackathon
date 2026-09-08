import pytest

from agents.orchestrator import run_studiosync


def test_demo_mode_is_explicit_and_provenance_aware():
    result = run_studiosync("Storm cancels Scene 42", mode="demo")
    assert result["integration"]["mode"] == "demo"
    assert result["approvals"]["status"] == "required"
    assert any(item["type"] == "synthetic" for item in result["provenance"])
    assert any(item["type"] == "mcp" for item in result["provenance"])


def test_live_mode_never_silently_returns_demo_data(monkeypatch):
    monkeypatch.delenv("GOOGLE_CLOUD_PROJECT", raising=False)
    monkeypatch.delenv("CLICKHOUSE_MCP_URL", raising=False)
    with pytest.raises(RuntimeError, match="Live mode requires"):
        run_studiosync("Storm cancels Scene 42", mode="live")
