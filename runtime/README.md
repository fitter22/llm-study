# C++ inference runtime

The runtime is a standalone C++17 CPU executable. The initial target is to load exported model weights and generate tokens without Python or PyTorch.

Implementation order:
1. Weight/configuration loader.
2. Uncached forward pass and greedy decoding.
3. Python/C++ numerical parity tests.
4. KV cache.
5. Raspberry Pi Zero 2 W deployment and profiling.

Build from the repository root with CMake. See issues #9–#12.
