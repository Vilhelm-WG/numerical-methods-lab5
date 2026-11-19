"""Завдання 1.1 — інтерполяційні многочлени Ньютона (відповідальна: Діана).

а) x = 0.248 -> перша формула Ньютона (вперед), вузол x0, q = 0
б) x = 2.8   -> друга формула Ньютона (назад), вузол x4
"""
import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

X = np.array([0.248, 0.923, 1.598, 2.273, 2.948])
Y = np.array([-3.642, 0.802, 0.841, 0.513, 0.328])
H = 0.675


def build_diff_table():
    """diff_table[i, j] = Δ^j y_i."""
    n = len(Y)
    table = np.zeros((n, n))
    table[:, 0] = Y
    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = table[i + 1, j - 1] - table[i, j - 1]
    return table


def newton_forward(x):
    """f'(x), f''(x) за першою формулою Ньютона (вузол x0)."""
    t = build_diff_table()
    q = (x - X[0]) / H
    dy, d2y, d3y, d4y = t[0, 1], t[0, 2], t[0, 3], t[0, 4]
    f1 = (1 / H) * (
        dy
        + ((2 * q - 1) / 2) * d2y
        + ((3 * q**2 - 6 * q + 2) / 6) * d3y
        + ((4 * q**3 - 18 * q**2 + 22 * q - 6) / 24) * d4y
    )
    f2 = (1 / H**2) * (
        d2y
        + (q - 1) * d3y
        + ((6 * q**2 - 18 * q + 11) / 12) * d4y
    )
    return float(f1), float(f2)


def newton_backward(x):
    """f'(x), f''(x) за другою формулою Ньютона (вузол x4)."""
    t = build_diff_table()
    q = (x - X[-1]) / H
    dy, d2y, d3y, d4y = t[3, 1], t[2, 2], t[1, 3], t[0, 4]
    f1 = (1 / H) * (
        dy
        + ((2 * q + 1) / 2) * d2y
        + ((3 * q**2 + 6 * q + 2) / 6) * d3y
        + ((4 * q**3 + 18 * q**2 + 22 * q + 6) / 24) * d4y
    )
    f2 = (1 / H**2) * (
        d2y
        + (q + 1) * d3y
        + ((6 * q**2 + 18 * q + 11) / 12) * d4y
    )
    return float(f1), float(f2)


def solve():
    """Єдиний інтерфейс для compare.py: {назва: (f', f'')}."""
    return {
        "1.1а f'(0.248), f''(0.248)": newton_forward(0.248),
        "1.1б f'(2.8), f''(2.8)": newton_backward(2.8),
    }


if __name__ == "__main__":
    print("=== ПУНКТ 1.1 а) x = 0.248 (перша формула Ньютона - вперед) ===")
    print(f"q = {(0.248 - X[0]) / H:g}")
    f1, f2 = newton_forward(0.248)
    print(f"f'(0.248)  = {f1:.4f}")
    print(f"f''(0.248) = {f2:.4f}\n")

    print("=== ПУНКТ 1.1 б) x = 2.8 (друга формула Ньютона - назад) ===")
    print(f"q = {(2.8 - X[-1]) / H:.5f}")
    f1, f2 = newton_backward(2.8)
    print(f"f'(2.8)  = {f1:.4f}")
    print(f"f''(2.8) = {f2:.4f}")