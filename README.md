# AIxTech Enhanced Crypto Trading Information System v5

> **v5 Enhanced** paper-only automated cryptocurrency trading information system with advanced multi-factor adaptive strategies per asset class (regime-aware clustering, multi-timeframe confluence, on-chain activity proxies, volatility forecasting, ML-inspired factor combinations, correlation filters), robust zero-trust cyber and data security architecture (enhanced redaction, multi-hash seals, anomaly detection with entropy, continuous attestation, encryption stubs), and full AI-agent harness principles inspired by [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo).
>
> **Research / paper-trading only.** No live order execution, no withdrawal permissions, no storage of exchange secrets, private keys, seeds, or personal data. Not financial, legal, or investment advice.

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![Licence](https://img.shields.io/badge/licence-MIT-green) ![Mode](https://img.shields.io/badge/execution-paper%20only-orange)

## Overview
Modular framework for crypto trading *information* and paper strategy evaluation. Builds on prior kkzee92 versions (v1-v4) and the AI-agent harness demo.

- **Expanded asset classes** with refined multi-factor adaptive strategies: Majors, Large Alts, DeFi, Stables, High-Vol/Meme, L2, RWA, Perpetuals, AI-tokens, GameFi, Restaking/Modular, and emerging.
- Secure data ingestion (public market data only, synthetic fixtures, automatic redaction of sensitive patterns).
- Adaptive risk management & position sizing (volatility targeting, correlation filters, regime awareness, anomaly gates, drawdown kill-switches, time-stops, portfolio-level correlation).
- Zero-trust cyber/data security architecture (layered controls, audit trails with multi-hash seals, anomaly stubs, entropy scoring).
- AI-agent safe development (AGENTS.md rules, disclosure trails, CI gates for lint, tests, secret scanning, license allow-list).
- Offline-capable simulation and demo hooks. Injectable I/O for testability.

## Quick Start
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src python -m crypto_trading demo
PYTHONPATH=src pytest tests/ -q --cov=src --cov-report=term-missing
```

## Architecture
See [docs/architecture.md](docs/architecture.md) and [docs/security-architecture.md](docs/security-architecture.md).

## Asset Class Strategies
See [docs/trading-strategies.md](docs/trading-strategies.md) for detailed multi-factor rules per class. Implementation in `src/crypto_trading/strategies.py`.

## Security
[SECURITY.md](SECURITY.md) — Zero Trust, least privilege, secrets via environment only, no private keys/seeds in code/prompts/fixtures, synthetic data only.

## AI Agent Rules
See [AGENTS.md](AGENTS.md). Human review required for merges. No production secrets, seeds, or personal data in prompts.

## Licence
[MIT](LICENSE)
