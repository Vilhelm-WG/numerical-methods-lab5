"""Задача 2.1 б) і 2.2 — формула трапецій (відповідальна: Софія). Порядок k = 2.

I = ∫_1^2 ln(x)/(1+x) dx

Формула трапецій (h = (b-a)/n, x_i = a + i*h, y_i = f(x_i)):
    I ≈ h * [ (y0 + yn)/2 + y1 + y2 + ... + y_{n-1} ]

Правило Рунге (k = 2):
    |I - I_2n| ≈ |I_2n - I_n| / (2^2 - 1) = |I_2n - I_n| / 3

Апріорна оцінка:
    |R| <= (b-a)^3 * M2 / (12 n^2),   M2 = max |f''(x)| на [a, b]
"""
import sys

from data2 import A, B, f, runge, d2, max_abs

# Щоб символи ∫, ≈ тощо коректно друкувались у консолі Windows (cp1251)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

K = 2       # порядок точності формули трапецій
EPS = 1e-3  # задана точність для 2.1 б)


def trap(n):
    """Складена формула трапецій при розбитті [A, B] на n рівних частин."""
    h = (B - A) / n
    return h * (f(A) / 2 + f(B) / 2 + sum(f(A + i * h) for i in range(1, n)))


def a_priori(n=5):
    """Апріорна оцінка похибки трапецій: (b-a)^3 * M2 / (12 n^2). Повертає (оцінка, M2)."""
    m2 = max_abs(d2)
    return (B - A)**3 * m2 / (12 * n**2), m2


def reference():
    """Еталонне значення інтеграла: трапеції з дуже дрібним кроком + уточнення Рунге."""
    t1, t2 = trap(20000), trap(40000)
    return t2 + (t2 - t1) / (2**K - 1)


def solve():
    n, val, err = runge(trap, K, EPS, verbose=False)
    return {"2.1б трапеції, eps=1e-3": (n, val, err)}


if __name__ == "__main__":
    print(f"2.1 б) Формула трапецій, eps = {EPS:g}, правило Рунге (k = {K})")
    n, val, err = runge(trap, K, EPS)
    print(f"  Умова {err:.2e} < {EPS:g} виконана при n = {n}:  I ≈ {val:.5f}")

    print("\n2.2 Апріорна оцінка, n = 5")
    print("  f''(x) = -1/(x^2(1+x)) - 2/(x(1+x)^2) + 2 ln x/(1+x)^3")
    for x in (1.0, 1.25, 1.5, 1.75, 2.0):
        print(f"    f''({x:.2f}) = {d2(x):+.5f}")
    r, m2 = a_priori(5)
    print(f"  M2 = max|f''| = |f''(1)| = {m2:.4f}")
    print(f"  |R| <= (b-a)^3 * M2 / (12 n^2) = 1 * {m2:.0f} / (12 * 25) = {r:.5f}")

    ref = reference()
    t5 = trap(5)
    print(f"\n  Еталон I ≈ {ref:.8f}")
    print(f"  Трапеції n = 5: I_5 = {t5:.8f}, фактична похибка = {abs(t5 - ref):.2e}"
          f" <= {r:.2e} (апріорна межа)")
