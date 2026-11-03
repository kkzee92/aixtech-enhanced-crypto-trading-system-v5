from crypto_trading.strategies import evaluate_strategy
from crypto_trading.features import compute_features

def test_majors_long():
    feats = {"trend_strength": 0.7, "regime": "neutral", "anomaly_score": 0.2, "mtf_confluence": 0.8, "momentum": 0.01, "volume_ratio": 1.5}
    sig = evaluate_strategy("majors", feats)
    assert sig["action"] == "long"
    assert sig["confidence"] > 0.5

def test_high_vol_flat():
    feats = {"trend_strength": 0.2, "regime": "high_vol", "anomaly_score": 0.3, "volume_ratio": 1.0}
    sig = evaluate_strategy("high_vol", feats)
    assert sig["action"] in ("flat", "small_long")

def test_anomaly_gate():
    feats = {"anomaly_score": 0.9, "trend_strength": 0.8}
    sig = evaluate_strategy("majors", feats)
    assert sig["action"] == "flat"
