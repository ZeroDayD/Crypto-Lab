"""
Low-exponent broadcast attack demo (e=3). Recovers plaintext when the same message is sent to >=3 distinct RSA moduli without padding.
Usage:
  python -m cryptolab_py.rsa.low_e --demo
"""
import argparse
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
from math import prod

def crt(remainders, moduli):
    N = prod(moduli)
    total = 0
    for a_i, n_i in zip(remainders, moduli):
        m_i = N // n_i
        inv = pow(m_i, -1, n_i)
        total += a_i * m_i * inv
    return total % N, N

def iroot(k, n):
    x = int(n ** (1.0/k))
    while (x+1)**k <= n:
        x += 1
    while x**k > n:
        x -= 1
    return x

def demo():
    e = 3
    msg = b"attack-at-dawn"
    m = bytes_to_long(msg)

    cts, ns = [], []
    for _ in range(3):
        key = RSA.generate(1024, e=e)
        n = key.n
        c = pow(m, e, n)
        ns.append(n)
        cts.append(c)

    x, N = crt(cts, ns)       # m^e modulo product of moduli
    m_rec = iroot(e, x)       # exact integer root
    print("Recovered:", long_to_bytes(m_rec))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if args.demo:
        demo()

if __name__ == "__main__":
    main()
