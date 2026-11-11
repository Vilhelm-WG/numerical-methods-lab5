"""Завдання 1.3 — прості формули (центральні різниці) (відповідальний: Вільгельм).

f'(x_i)  ≈ (y_{i+1} - y_{i-1}) / (2h)
f''(x_i) ≈ (y_{i+1} - 2 y_i + y_{i-1}) / h^2
"""
from data import X, Y, H


def central(x):
    i = X.index(x)
    f1 = (Y[i + 1] - Y[i - 1]) / (2 * H)
    f2 = (Y[i + 1] - 2 * Y[i] + Y[i - 1]) / H**2
    return f1, f2


def solve():
    return {
        "1.3а f'(1.598), f''(1.598)": central(1.598),
        "1.3б f'(2.273), f''(2.273)": central(2.273),
    }


if __name__ == "__main__":
    for name, (f1, f2) in solve().items():
        print(f"{name}: f' = {f1:.4f}, f'' = {f2:.4f}")
