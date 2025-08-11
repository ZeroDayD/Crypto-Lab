"""
RSA key generation and basic encrypt/decrypt demo.
Usage:
  python -m cryptolab_py.rsa.keygen --bits 2048 --outprefix mykey
"""
import argparse
from Crypto.PublicKey import RSA

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--bits", type=int, default=2048)
    p.add_argument("--outprefix", default="rsa_key")
    args = p.parse_args()

    key = RSA.generate(args.bits)
    open(f"{args.outprefix}_priv.pem", "wb").write(key.export_key())
    open(f"{args.outprefix}_pub.pem", "wb").write(key.publickey().export_key())
    print(f"Wrote {args.outprefix}_priv.pem and {args.outprefix}_pub.pem")

if __name__ == "__main__":
    main()
