# Architecture notes

The v0.1 model is a decoder-only Transformer trained from random initialization with next-token prediction.

## Baseline

- Byte-level vocabulary: 257 tokens (256 byte values plus EOD).
- Context length: 256 tokens/bytes.
- Four Transformer blocks and four attention heads.
- Embedding dimension 128 and feed-forward dimension 512.
- Causal self-attention, residual connections, LayerNorm and GELU.
- Tied token embedding and output projection weights.
- FP32 baseline.

The implementation should expose tensor shapes and intermediate operations for learning. See issue #6 for the architecture task and issue #1 for the overall acceptance criteria.

## Training versus inference

Training uses PyTorch and automatic differentiation on a development computer. Deployment uses a separate C++17 inference runtime with a documented exported-weight format. The Pi must not need PyTorch.
