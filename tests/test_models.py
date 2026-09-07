from core.models import BudgetDelta

def test_budget_delta():
    b=BudgetDelta(baseline=100,revised=125,delta=25)
    assert b.delta == 25
