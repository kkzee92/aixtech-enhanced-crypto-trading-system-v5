"""Risk gates and position sizing for paper signals. v5."""

from typing import Dict, Any

def apply_risk_gates(signal: Dict[str, Any], risk_metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Apply volatility targeting, drawdown, anomaly, and correlation gates."""
    result = signal.copy()
    drawdown = risk_metrics.get("drawdown", 0.0)
    correlation = risk_metrics.get("portfolio_correlation", 0.0)

    if drawdown > 0.12:
        result.update(action="flat", confidence=1.0, reason="drawdown kill-switch")
    elif signal.get("anomaly_score", 0) > 0.75 or result.get("factors", []).count("anomaly") > 0 and signal.get("anomaly_score", 0) > 0.6:
        result.update(action="flat", confidence=0.9, reason="anomaly risk gate")
    elif correlation > 0.8 and result.get("action") == "long":
        result["confidence"] = max(0.0, result.get("confidence", 0) * 0.5)
        result["reason"] += " | high portfolio correlation filter"

    # Vol targeting
    if signal.get("regime") == "high_vol":
        result["confidence"] = max(0.0, result.get("confidence", 0) * 0.55)
    elif signal.get("regime") == "low_vol":
        result["confidence"] = min(1.0, result.get("confidence", 0) * 1.1)

    return result
