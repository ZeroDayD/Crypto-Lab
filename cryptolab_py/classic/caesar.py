"""
Caesar cipher with CLI encrypt/decrypt and brute-force crack.
Usage:
  python -m cryptolab_py.classic.caesar --encrypt --shift 13 --text "HELLO"
  python -m cryptolab_py.classic.caesar --decrypt --shift 13 --text "URYYB"
  python -m cryptolab_py.classic.caesar --crack --text "URYYB"
"""
import argparse
import string
from collections import Counter

ALPHABET = string.ascii_uppercase

def caesar(s: str, shift: int, decrypt: bool=False) -> str:
    shift = (-shift) if decrypt else shift
    res = []
    for ch in s:
        up = ch.upper()
        if up in ALPHABET:
            idx = (ALPHABET.index(up) + shift) % 26
            out = ALPHABET[idx]
            res.append(out if ch.isupper() else out.lower())
        else:
            res.append(ch)
    return ''.join(res)

def score_english(text: str) -> float:
    # Rough etaoin scoring
    freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    c = Counter([ch for ch in text.upper() if ch in ALPHABET])
    total = sum(c.values()) or 1
    score = 0.0
    for i, letter in enumerate(freq):
        score += (c[letter] / total) * (len(freq)-i)
    return score

def crack(cipher: str, top: int=5):
    candidates = []
    for shift in range(26):
        pt = caesar(cipher, shift, decrypt=True)
        candidates.append((score_english(pt), shift, pt))
    candidates.sort(reverse=True)
    return candidates[:top]

def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--encrypt", action="store_true")
    g.add_argument("--decrypt", action="store_true")
    g.add_argument("--crack", action="store_true")
    p.add_argument("--shift", type=int, default=13)
    p.add_argument("--text", required=True)
    p.add_argument("--top", type=int, default=5)
    args = p.parse_args()

    if args.encrypt:
        print(caesar(args.text, args.shift))
    elif args.decrypt:
        print(caesar(args.text, args.shift, decrypt=True))
    else:
        for score, shift, pt in crack(args.text, args.top):
            print(f"[shift={shift:2d}] {pt}  (score={score:.3f})")

if __name__ == "__main__":
    main()
