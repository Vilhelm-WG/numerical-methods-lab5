"""Задача 2.1 а) і 2.2 — формула прямокутників (відповідальна: Діана).
Основна: середніх прямокутників (порядок k = 2). Додатково: лівих (k = 1).
"""
from data2 import A, B, f, runge, d1, d2, max_abs


def rect_mid(n):
    h = (B - A) / n
    return h * sum(f(A + (i + 0.5) * h) for i in range(n))


def rect_left(n):
    h = (B - A) / n
    return h * sum(f(A + i * h) for i in range(n))


def a_priori(n=5):
    """Апріорні оцінки похибки при розбитті на n частин."""
    m2, m1 = max_abs(d2), max_abs(d1)
    mid = (B - A)**3 * m2 / (24 * n**2)    # середніх прямокутників
    left = (B - A)**2 * m1 / (2 * n)       # лівих прямокутників
    return mid, left, m2, m1


def solve():
    n, val, err = runge(rect_mid, 2, 1e-2, verbose=False)
    return {"2.1а прямокутники (середніх), eps=1e-2": (n, val, err)}


if __name__ == "__main__":
    print("2.1 а) середні прямокутники, eps = 1e-2")
    runge(rect_mid, 2, 1e-2)
    print("\nДодатково: ліві прямокутники (k = 1), eps = 1e-2")
    runge(rect_left, 1, 1e-2)
    mid, left, m2, m1 = a_priori(5)
    print(f"\n2.2 n = 5: M2 = {m2:.4f} -> |R| <= (b-a)^3*M2/(24 n^2) = {mid:.5f}")
    print(f"          (ліві) M1 = {m1:.4f} -> |R| <= (b-a)^2*M1/(2n) = {left:.5f}")
