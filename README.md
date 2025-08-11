# cryptolab-py

Hands-on cryptography lab in Python. Each module lets you create and break primitives.

Run modules:
```
python -m cryptolab_py.classic.caesar --help
python -m cryptolab_py.symmetric.aes_gcm --help
python -m cryptolab_py.rsa.keygen --help
python -m cryptolab_py.rsa.low_e --demo
```

## Layout
- classic/ — Caesar, Vigenere (+ crackers)
- rng/ — LCG, prediction (planned)
- symmetric/ — AES (CBC/GCM), ChaCha20 (planned), padding-oracle lab (planned)
- modes/ — ECB/CBC/CTR/GCM demos (planned)
- hash/ — length-extension, rainbow (planned)
- rsa/ — keygen, low-e, common-modulus
- keyexchange/ — DH/ECDH + MITM (planned)
- ecc/ — ECDSA + nonce-reuse attack (planned)
- pki/ — mini-CA (planned)
- apps/ — OpenSSH, WireGuard, Signal-level (planned)
- pqc/ — Kyber/Dilithium (planned)
- cryptoassets/ — secp256k1, BTC addresses/signatures (planned)

## Setup
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
