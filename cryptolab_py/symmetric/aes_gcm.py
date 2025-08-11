"""
AES-GCM CLI using PyCryptodome.
Usage:
  echo -n "secret message" | python -m cryptolab_py.symmetric.aes_gcm --encrypt --keyhex <64 hex> --noncehex <24 hex> > out.bin
  python -m cryptolab_py.symmetric.aes_gcm --decrypt --keyhex <64 hex> --noncehex <24 hex> --infile out.bin
If key/nonce not provided, they are generated.
"""
import argparse, sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(data: bytes, key: bytes=None, nonce: bytes=None) -> bytes:
    key = key or get_random_bytes(32)
    nonce = nonce or get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(data)
    return b"".join([b"KEY", key, b"NON", nonce, b"TAG", tag, b"CT", ct])

def decrypt(packed: bytes) -> bytes:
    rest = packed
    assert rest.startswith(b"KEY"), "bad format"
    rest = rest[3:]
    key, rest = rest[:32], rest[32:]
    assert rest.startswith(b"NON"), "bad format"
    rest = rest[3:]
    nonce, rest = rest[:12], rest[12:]
    assert rest.startswith(b"TAG"), "bad format"
    rest = rest[3:]
    tag, rest = rest[:16], rest[16:]
    assert rest.startswith(b"CT"), "bad format"
    ct = rest[2:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ct, tag)

def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--encrypt", action="store_true")
    g.add_argument("--decrypt", action="store_true")
    p.add_argument("--keyhex", help="64 hex chars for 256-bit key")
    p.add_argument("--noncehex", help="24 hex chars for 96-bit nonce")
    p.add_argument("--infile")
    args = p.parse_args()

    if args.encrypt:
        data = sys.stdin.buffer.read()
        key = bytes.fromhex(args.keyhex) if args.keyhex else None
        nonce = bytes.fromhex(args.noncehex) if args.noncehex else None
        out = encrypt(data, key, nonce)
        sys.stdout.buffer.write(out)
    else:
        data = open(args.infile, "rb").read() if args.infile else sys.stdin.buffer.read()
        pt = decrypt(data)
        sys.stdout.buffer.write(pt)

if __name__ == "__main__":
    main()
