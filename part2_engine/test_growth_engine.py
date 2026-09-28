import os
import tempfile
from growth_engine import mom_growth, is_flagged, validate_feed

def test_ethnic_april_may():
    assert mom_growth(104520.77, 185107.61) == 77.1
    assert is_flagged(mom_growth(104520.77, 185107.61)) == "flagged"

def test_beauty_may_june():
    assert mom_growth(35542.11, 37559.07) == 5.67
    assert is_flagged(mom_growth(35542.11, 37559.07)) == "not_flagged"

def test_exact_boundary():
    assert mom_growth(100000, 108000) == 8.0
    assert is_flagged(8.0) == "escalate_exact_boundary"

def test_corrupted_feed():
    path = os.path.join(os.path.dirname(__file__), "fixtures", "corrupted_feed.csv")
    ok, errors = validate_feed(path)
    assert ok is False
    assert errors == [
        "line 3: negative revenue (-4200.0) for category=Western Wear",
        "line 4: missing category (month=July)",
        "line 6: missing revenue (category=Home & Kitchen)",
    ]
