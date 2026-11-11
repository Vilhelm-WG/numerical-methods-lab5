"""Завдання 1.2 — інтерполяційний многочлен Стірлінга (відповідальна: Софія).

x = 1.598 — центральний вузол x2, тому q = 0.
"""
from data import X, Y, H, diff_table


def stirling(x=1.598):
    d = diff_table()
    i = X.index(x)  # центральний вузол; q = 0
    # Δy_{i-1}, Δy_i
    d1_mid = (d[0][i - 1] + d[0][i]) / 2
    # Δ^3 y_{i-2}, Δ^3 y_{i-1}
    d3_mid = (d[2][i - 2] + d[2][i - 1]) / 2
    f1 = (d1_mid - d3_mid / 6) / H
    # Δ^2 y_{i-1}, Δ^4 y_{i-2}
    f2 = (d[1][i - 1] - d[3][i - 2] / 12) / H**2
    return f1, f2


def solve():
    return {"1.2 f'(1.598), f''(1.598)": stirling(1.598)}


if __name__ == "__main__":
    for name, (f1, f2) in solve().items():
        print(f"{name}: f' = {f1:.4f}, f'' = {f2:.4f}")
