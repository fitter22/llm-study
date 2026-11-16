"""Initial repository smoke tests."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_baseline_config_is_present_and_consistent() -> None:
    config_path = ROOT / "configs" / "tiny-byte.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))

    model = config["model"]
    tokenizer = config["tokenizer"]

    assert model["vocab_size"] == 257
    assert model["context_length"] == 256
    assert model["n_layers"] == 4
    assert model["n_heads"] == 4
    assert model["embedding_dim"] == 128
    assert tokenizer["end_of_document_id"] == 256
    assert tokenizer["byte_token_max"] + 1 == tokenizer["end_of_document_id"]
