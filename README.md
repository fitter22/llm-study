# TinyGPT Study

An educational project to build a tiny GPT-style language model from random initialization, train it on an English text corpus, and run it offline on a Raspberry Pi Zero 2 W.

The objective is to understand language-model training and inference, not to produce a ChatGPT-quality assistant.

## v0.1 design

- Decoder-only Transformer implemented in PyTorch using explicit tensor operations.
- Byte tokenizer: IDs 0–255 represent byte values; ID 256 is end-of-document (EOD).
- Baseline: 4 layers, 4 attention heads, 128 embedding dimensions, 512-dimensional MLP and 256-byte context.
- FP32 training with AdamW and a fixed seed.
- Custom C++17 CPU inference runtime, independent of PyTorch.
- Target: Raspberry Pi Zero 2 W with Raspberry Pi OS Lite 64-bit.

See [the v0.1 epic](https://github.com/fitter22/llm-study/issues/1) for the plan and implementation tasks.

## Repository layout

- configs/ — model and experiment configurations.
- data/raw/ — user-provided text corpus (not committed).
- data/processed/ — generated datasets and manifests (not committed).
- src/tinygpt/ — Python tokenizer, dataset, models, training and evaluation.
- runtime/ — standalone C++ inference runtime.
- tests/ — automated tests.
- scripts/ — development and deployment helpers.
- docs/ — architecture, training, inference and experiment notes.
- artifacts/ — checkpoints, exports and generated samples (not committed).

## Development setup

Use Python 3.11 or another version supported by the selected PyTorch release.

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install -e ".[dev]"

Run tests:

    pytest

Build the C++ runtime:

    cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
    cmake --build build

The initial C++ executable is a scaffold; inference is implemented in later milestones.

## Data and generated artifacts

Place UTF-8 plain-text documents in data/raw/. Do not commit private or copyrighted corpora unless you have permission to distribute them. Processed datasets, checkpoints, exported weights and generated samples are ignored by Git by default.

## Learning sequence

1. Prepare a clean corpus and byte tokenizer.
2. Train a bigram baseline.
3. Implement and train the Transformer from scratch.
4. Evaluate controlled experiments.
5. Export weights to a documented portable format.
6. Implement and validate C++ inference.
7. Add KV caching and deploy to the Pi.

## Corpus provenance

Record source, authorship, licensing and usage permissions for every training document. The source-code license and training-corpus terms should be settled before a public v0.1 release.
