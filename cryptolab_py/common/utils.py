"""Common helpers for cryptolab-py."""
from typing import Iterable

def chunks(b: bytes, size: int) -> Iterable[bytes]:
    for i in range(0, len(b), size):
        yield b[i:i+size]
