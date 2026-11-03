"""Feature computation for multi-factor strategies (synthetic / public data). v5 enhancements."""

from typing import List, Dict, Any
import statistics
import math

def compute_features(prices: List[float], volumes: List[float] = None, multi_tf: bool = False) -> Dict[str, Any]:
    """Compute trend, momentum, volatility, regime, anomaly, and proxies."""
    if not prices or len(prices) < 2:
        return {"trend_strength": 0.0, "regime": "unknown", "anomaly_score": 0.0, "volatility": 0.0}

    returns = [(prices[i] - prices[i-1]) / prices[i-1] for i in range(1, len(prices))]
    vol = statistics.stdev(returns) if len(returns) > 1 else 0.0
    trend = (prices[-1] - prices[0]) / prices[0] if prices[0] else 0.0
    trend_strength = min(1.0, abs(trend) / (vol + 1e-6))

    # Regime via volatility clustering proxy
    if vol < 0.015:
        regime = "low_vol"
    elif vol > 0.06:
        regime = "high_vol"
    else:
        regime = "neutral"

    # Anomaly: z-score like
    if returns:
        mean_ret = statistics.mean(returns)
        std_ret = vol or 1e-6
        z = abs(returns[-1] - mean_ret) / std_ret
        anomaly_score = min(1.0, z / 4.0)
    else:
        anomaly_score = 0.0

    # Volume proxy
    vol_ratio = 1.0
    if volumes and len(volumes) > 1:
        avg_vol = statistics.mean(volumes[:-1]) or 1
        vol_ratio = volumes[-1] / avg_vol

    # Simple momentum
    momentum = returns[-1] if returns else 0.0

    features = {
        "trend_strength": round(trend_strength, 3),
        "regime": regime,
        "anomaly_score": round(anomaly_score, 3),
        "volatility": round(vol, 4),
        "last_return": round(returns[-1], 4) if returns else 0.0,
        "momentum": round(momentum, 4),
        "volume_ratio": round(vol_ratio, 2),
        "mtf_confluence": 0.7 if multi_tf else 0.5,  # stub
    }
    return features
