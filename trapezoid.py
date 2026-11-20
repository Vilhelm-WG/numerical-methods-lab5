"""Задача 2.1 б) і 2.2 — формула трапецій (відповідальна: Софія). Порядок k = 2."""
from data2 import A, B, f, runge, d2, max_abs


def trap(n):
    h = (B - A) / n
    return h * (f(A) / 2 + f(B) / 2 + sum(f(A + i * h) for i in range(1, n)))


def a_priori(n=5):
    m2 = max_abs(d2)
    return (B - A)**3 * m2 / (12 * n**2), m2


def solve():
    n, val, err = runge(trap, 2, 1e-3, verbose=False)
    return {"2.1б трапеції, eps=1e-3": (n, val, err)}


if __name__ == "__main__":
    print("2.1 б) трапеції, eps = 1e-3")
    runge(trap, 2, 1e-3)
    r, m2 = a_priori(5)
    print(f"\n2.2 n = 5: M2 = {m2:.4f} -> |R| <= (b-a)^3*M2/(12 n^2) = {r:.5f}")
