"""Demo runner for paper signals."""

from .features import compute_features
from .strategies import evaluate_strategy
from .risk import apply_risk_gates
from .security import redact_sensitive, multi_hash_seal

def run_demo():
    # Synthetic prices
    prices = [100.0, 101.5, 103.0, 102.2, 105.5, 108.0, 107.5, 110.0]
    features = compute_features(prices)
    print("Features:", features)

    for cls in ["majors", "high_vol", "defi", "stables", "large_alts", "l2", "ai_tokens"]:
        signal = evaluate_strategy(cls, features)
        gated = apply_risk_gates(signal, {"drawdown": 0.05})
        print(f"{cls}: {gated}")

    log = "Sample log with no secrets"
    sealed = multi_hash_seal(log)
    print("Seal:", sealed)
    print("Redacted:", redact_sensitive("normal text 0x" + "a"*64))
