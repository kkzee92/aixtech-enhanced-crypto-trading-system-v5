# Security Architecture (v5 Enhanced)

## Zero-Trust Model
Verify explicitly, least privilege, assume breach. Continuous attestation of data sources and code integrity via multi-hash seals.

## Layers
1. **Ingestion**: Schema/range validation, automatic redaction of high-entropy strings, private-key-like patterns, seed phrases, API key formats.
2. **Processing**: Isolated feature computation. Network access only via injectable, audited fetchers. No side effects.
3. **Strategies & Risk**: Pure functions producing paper signals. No order placement paths.
4. **Audit**: Immutable hash-chained logs with multi-hash seals (SHA-256, SHA3-256, BLAKE2b, SHA-512). Anomaly detection stubs on length, Shannon entropy, residual patterns.
5. **Encryption**: TLS for any external calls. AES-GCM style stubs for any local sensitive material (none stored by design).

## Controls
- CI secret scanning (gitleaks-style patterns).
- Licence allow-list.
- Policy guard adapted for crypto secrets (no seeds, mnemonics, private keys, exchange credentials).
- Dependency scanning.
- Human review mandatory.
- Redaction on any log or output path.
- Entropy-based anomaly scoring.

## Redaction Patterns
- Base58-like strings >40 chars
- Hex strings of private-key length (32+ chars)
- Common seed phrase word sequences (BIP39 style, expanded)
- High-entropy sequences
- API key / secret / token patterns

Implementation in `src/crypto_trading/security.py`.
