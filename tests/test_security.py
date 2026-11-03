from crypto_trading.security import redact_sensitive, multi_hash_seal, anomaly_score

def test_redact_hex():
    text = "secret 0x" + "a"*64 + " more"
    red = redact_sensitive(text)
    assert "[REDACTED_HEX]" in red
    assert "aaaa" not in red

def test_multi_hash():
    seals = multi_hash_seal("test data")
    assert "sha256" in seals
    assert len(seals["sha256"]) == 64

def test_anomaly():
    score = anomaly_score("a" * 100)
    assert 0 <= score <= 1
