# Architecture Overview (v5)

Modular, injectable design for paper-only crypto trading information.

- `features.py`: Compute multi-factor features from price/volume series (synthetic or public).
- `strategies.py`: Asset-class specific signal generators (pure functions).
- `risk.py`: Gates for drawdown, anomaly, correlation, volatility targeting.
- `security.py`: Redaction, multi-hash seals, anomaly scoring.
- `demo.py` / CLI: Offline demonstration.
- Tests: Unit coverage for strategies and security.
- CI: Pytest + coverage + secret scan placeholder.

All I/O is injectable; no live network or execution by default.
