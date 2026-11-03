# AI Agent Rules (inspired by zeekiankok92 harness)

This repository is for paper-only research and information systems. Agents must follow these rules:

1. **No secrets**: Never include private keys, seed phrases, API keys, exchange credentials, or high-entropy sensitive strings in code, comments, prompts, logs, or fixtures.
2. **Synthetic data only**: Use only synthetic or public market data. No production personal or customer data.
3. **Paper-only**: No code that places live orders, requests withdrawal permissions, or connects to exchange trading endpoints with real credentials.
4. **Disclosure**: All AI-assisted changes must include `AI-Assisted:` trailer or update docs/ai-disclosure-log.md.
5. **Human review**: Definition of Done requires CI green + human approval (see harness/definition-of-done.md).
6. **Security first**: Prefer redaction, validation, and audit logging. Run secret scanners.
7. **Minimal dependencies**: Prefer stdlib where possible; document any third-party licences.

Agents should produce testable, auditable code with clear acceptance criteria in task briefs.
