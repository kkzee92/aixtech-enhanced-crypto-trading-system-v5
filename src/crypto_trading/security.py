"""Security utilities: enhanced redaction, multi-hash seals, anomaly stubs. v5."""

import hashlib
import re
import math
from typing import Dict

def redact_sensitive(text: str) -> str:
    """Redact potential private keys, seeds, high-entropy strings, API keys."""
    # Base58-like (private keys, addresses)
    text = re.sub(r'[1-9A-HJ-NP-Za-km-z]{40,}', '[REDACTED_KEY]', text)
    # Hex private keys / long hex
    text = re.sub(r'(0x)?[0-9a-fA-F]{32,}', '[REDACTED_HEX]', text)
    # BIP39 seed phrase patterns (extended common words)
    seed_words = r'(abandon|ability|able|about|above|absent|absorb|abstract|absurd|abuse|access|accident|account|accuse|achieve|acid|acoustic|acquire|across|act|action|actor|actress|actual)'
    text = re.sub(rf'\b{seed_words}\b(?:\s+\w+){{11,23}}', '[REDACTED_SEED]', text, flags=re.IGNORECASE)
    # API key like patterns
    text = re.sub(r'(?i)(api[_-]?key|secret|token)\s*[:=]\s*\S+', '[REDACTED_API]', text)
    return text

def multi_hash_seal(data: str) -> Dict[str, str]:
    """Generate multi-hash seals for audit trails."""
    encoded = data.encode('utf-8')
    return {
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "sha3_256": hashlib.sha3_256(encoded).hexdigest(),
        "blake2b": hashlib.blake2b(encoded).hexdigest(),
        "sha512": hashlib.sha512(encoded).hexdigest()[:64],  # truncated for display
    }

def anomaly_score(log_entry: str) -> float:
    """Anomaly score based on length, entropy, and patterns."""
    if not log_entry:
        return 0.0
    if len(log_entry) > 2000:
        return 0.98
    # Shannon entropy proxy
    if len(log_entry) > 0:
        freq = {}
        for c in log_entry:
            freq[c] = freq.get(c, 0) + 1
        entropy = -sum((count / len(log_entry)) * math.log2(count / len(log_entry)) for count in freq.values())
        max_entropy = math.log2(len(set(log_entry)) or 1)
        entropy_ratio = entropy / (max_entropy or 1)
        if entropy_ratio > 0.85 and len(log_entry) > 100:
            return min(1.0, 0.6 + (entropy_ratio - 0.85) * 2)
    unique_ratio = len(set(log_entry)) / max(1, len(log_entry))
    if unique_ratio > 0.75 and len(log_entry) > 150:
        return 0.7
    return 0.05
