"""Asset-class specific multi-factor adaptive strategy stubs (paper signals only). v5 enhancements."""

from typing import Dict, Any

def evaluate_strategy(asset_class: str, features: Dict[str, Any]) -> Dict[str, Any]:
    """Return paper signal based on asset class with regime awareness and multi-factor scoring."""
    regime = features.get("regime", "neutral")
    trend = features.get("trend_strength", 0.0)
    anomaly = features.get("anomaly_score", 0.0)
    momentum = features.get("momentum", 0.0)
    vol_ratio = features.get("volume_ratio", 1.0)
    mtf = features.get("mtf_confluence", 0.5)

    signal = {
        "class": asset_class,
        "regime": regime,
        "action": "hold",
        "confidence": 0.0,
        "reason": "baseline",
        "factors": []
    }

    # Common filters
    if anomaly > 0.85:
        signal.update(action="flat", confidence=1.0, reason="hard anomaly gate", factors=["anomaly"])
        return signal

    if asset_class == "majors":
        if trend > 0.5 and regime != "high_vol" and mtf > 0.6 and anomaly < 0.5:
            conf = min(0.9, 0.45 + trend * 0.35 + mtf * 0.2)
            signal.update(
                action="long",
                confidence=round(conf, 2),
                reason="adaptive EMA + low/neutral vol regime + MTF confluence + vol targeting",
                factors=["trend", "regime", "mtf", "anomaly"]
            )
        elif regime == "high_vol" and trend < 0.25 and momentum < 0:
            signal.update(action="small_short", confidence=0.45, reason="high vol mean-reversion overlay", factors=["regime", "momentum"])
    elif asset_class == "high_vol":
        if vol_ratio > 2.5 and trend > 0.35 and regime == "high_vol" and anomaly < 0.6:
            signal.update(action="small_long", confidence=0.3, reason="volume burst + strict risk + time-stop proxy", factors=["volume", "trend", "regime"])
        else:
            signal.update(action="flat", confidence=0.7, reason="high_vol default flat")
    elif asset_class == "defi":
        if trend > 0.45 and anomaly < 0.45 and vol_ratio > 1.2:
            signal.update(action="long", confidence=0.6, reason="TVL/fee proxy + price strength + volume", factors=["trend", "volume", "anomaly"])
    elif asset_class == "stables":
        if anomaly > 0.35 or abs(momentum) > 0.005:
            signal.update(action="alert", confidence=0.95, reason="potential depeg / anomaly / flow", factors=["anomaly", "momentum"])
    elif asset_class == "large_alts":
        if trend > 0.55 and regime != "high_vol" and mtf > 0.55:
            signal.update(action="long", confidence=0.65, reason="relative strength vs BTC + MTF", factors=["trend", "mtf", "regime"])
    elif asset_class == "l2":
        if trend > 0.5 and regime == "neutral" and anomaly < 0.4:
            signal.update(action="long", confidence=0.5, reason="relative strength vs ETH + ecosystem", factors=["trend", "regime"])
    elif asset_class == "ai_tokens":
        if trend > 0.4 and vol_ratio > 1.5 and anomaly < 0.55:
            signal.update(action="long", confidence=0.4, reason="narrative + volume burst + activity proxy", factors=["trend", "volume"])
    elif asset_class == "perpetuals":
        if abs(momentum) < 0.01 and regime != "high_vol":
            signal.update(action="carry", confidence=0.55, reason="funding carry + contained drift", factors=["momentum", "regime"])
    else:
        if trend > 0.48 and anomaly < 0.5 and mtf > 0.5:
            signal.update(action="long", confidence=0.35, reason="generic multi-factor", factors=["trend", "mtf", "anomaly"])

    return signal
