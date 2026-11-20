"""Задача 2.1 в) і 2.2 — формула Сімпсона (відповідальний: Вільгельм). Порядок k = 4."""
from data2 import A, B, f, runge, d4, max_abs


def simpson(n):
    """n - парне число частин."""
    h = (B - A) / n
    s = f(A) + f(B)
    s += 4 * sum(f(A + i * h) for i in range(1, n, 2))
    s += 2 * sum(f(A + i * h) for i in range(2, n, 2))
    return h / 3 * s


def a_priori(n=6):
    m4 = max_abs(d4)
    return (B - A)**5 * m4 / (180 * n**4), m4


def solve():
    n, val, err = runge(simpson, 4, 1e-4, verbose=False)
    return {"2.1в Сімпсон, eps=1e-4": (n, val, err)}


if __name__ == "__main__":
    print("2.1 в) Сімпсон, eps = 1e-4")
    runge(simpson, 4, 1e-4)
    r, m4 = a_priori(6)
    print(f"\n2.2 n = 6: M4 = {m4:.4f} -> |R| <= (b-a)^5*M4/(180 n^4) = {r:.3e}")
