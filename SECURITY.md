# Security Policy

## Supported Versions
Only the latest main branch is supported for research purposes.

## Reporting a Vulnerability
Please open a private issue or contact the maintainer. Do not disclose details publicly until patched.

## Design Principles
- Zero-trust: verify explicitly, least privilege, assume breach.
- No private keys, seeds, mnemonics, or exchange credentials ever stored or logged.
- Automatic redaction of sensitive patterns.
- Multi-hash audit seals.
- Paper-only signals; no execution paths.
