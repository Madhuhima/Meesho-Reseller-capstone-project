import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "part2_engine"))
from mock_agent_runner import run

BASE = os.path.join(os.path.dirname(__file__), "..", "part2_engine", "fixtures")
def p(name): return os.path.join(BASE, name)

def test_may_scenario():
    out = run("May", p("april_category_revenue.csv"), p("may_category_revenue.csv"))
    assert out["validation_status"] == "valid"
    assert [x["category"] for x in out["flagged_categories"]] == ["Ethnic Wear","Western Wear","Kids Wear"]
    assert [x["mom_pct"] for x in out["flagged_categories"]] == [77.1,-23.6,-23.48]
    assert set(out["suppressed_categories"]) == {"Beauty & Personal Care","Home & Kitchen"}

def test_june_scenario():
    out = run("June", p("may_category_revenue.csv"), p("june_category_revenue.csv"))
    assert [x["category"] for x in out["flagged_categories"]] == ["Ethnic Wear","Home & Kitchen","Kids Wear"]
    assert [x["mom_pct"] for x in out["flagged_categories"]] == [-58.74,42.59,23.9]
    assert out["suppressed_categories"] == ["Western Wear"]
    assert out["escalated_categories"] == []

def test_hard_stop():
    out = run("July", p("june_category_revenue.csv"), p("corrupted_feed.csv"))
    assert out["validation_status"] == "invalid"
    assert out["action_taken"] == "hard_stop"
    assert len(out["validation_errors"]) == 3
    assert out["flagged_categories"] == []
    assert out["suppressed_categories"] == []
