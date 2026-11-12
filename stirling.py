"""Завдання 1.2 — інтерполяційний многочлен Стірлінга (відповідальна: Софія).

x = 1.598 — центральний вузол x2 (середина таблиці), тому q = (x - x2)/h = 0.

Формули Стірлінга для похідних при q = 0 (x0 — центральний вузол):
    f'(x0)  ≈ (1/h)   * [ (Δy_{-1} + Δy_0)/2 - (1/6) * (Δ³y_{-2} + Δ³y_{-1})/2 ]
    f''(x0) ≈ (1/h^2) * [ Δ²y_{-1} - (1/12) * Δ⁴y_{-2} ]

У нумерації таблиці (центр i = 2):
    Δy1, Δy2;  Δ²y1;  Δ³y0, Δ³y1;  Δ⁴y0.
"""
import sys

from data import X, Y, H, diff_table

# Щоб символи Δ, ² тощо коректно друкувались у консолі Windows (cp1251)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def stirling(x=1.598, verbose=False):
    """Повертає (f'(x), f''(x)) за формулами Стірлінга при q = 0."""
    if x not in X:
        raise ValueError("x має бути вузлом таблиці (q = 0)")
    d = diff_table()
    i = X.index(x)  # центральний вузол; q = 0
    if i < 2 or i > len(X) - 3:
        raise ValueError("для Δ⁴ потрібно по 2 вузли з кожного боку від x")

    q = (x - X[i]) / H  # = 0

    dy_l, dy_r = d[0][i - 1], d[0][i]      # Δy_{i-1}, Δy_i
    d2y = d[1][i - 1]                       # Δ²y_{i-1}
    d3y_l, d3y_r = d[2][i - 2], d[2][i - 1]  # Δ³y_{i-2}, Δ³y_{i-1}
    d4y = d[3][i - 2]                       # Δ⁴y_{i-2}

    d1_mid = (dy_l + dy_r) / 2
    d3_mid = (d3y_l + d3y_r) / 2

    f1 = (d1_mid - d3_mid / 6) / H
    f2 = (d2y - d4y / 12) / H**2

    if verbose:
        print(f"Центральний вузол x{i} = {X[i]}, y{i} = {Y[i]}, h = {H}, q = {q:g}")
        print(f"Δy{i-1} = {dy_l:.3f}, Δy{i} = {dy_r:.3f}  ->  середнє = {d1_mid:.4f}")
        print(f"Δ³y{i-2} = {d3y_l:.3f}, Δ³y{i-1} = {d3y_r:.3f}  ->  середнє = {d3_mid:.4f}")
        print(f"Δ²y{i-1} = {d2y:.3f},  Δ⁴y{i-2} = {d4y:.3f}")
        print(f"f'  = ({d1_mid:.4f} - {d3_mid:.4f}/6) / {H} "
              f"= {d1_mid - d3_mid / 6:.4f} / {H} = {f1:.4f}")
        print(f"f'' = ({d2y:.3f} - ({d4y:.3f})/12) / {H}^2 "
              f"= {d2y - d4y / 12:.4f} / {H**2:.6f} = {f2:.4f}")
    return f1, f2


def solve():
    return {"1.2 f'(1.598), f''(1.598)": stirling(1.598)}


if __name__ == "__main__":
    print("Таблиця скінченних різниць:")
    for k, row in enumerate(diff_table(), start=1):
        print(f"  Δ^{k} y:", [round(v, 6) for v in row])
    print()
    stirling(1.598, verbose=True)
    print()
    for name, (f1, f2) in solve().items():
        print(f"{name}: f' = {f1:.4f}, f'' = {f2:.4f}")
