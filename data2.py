"""Спільні дані Задачі 2, варіант 3 (відповідальний: Вільгельм).
I = ∫_1^2 ln(x)/(1+x) dx.  НЕ змінювати без погодження з TeamLead.
"""
import math

A, B = 1.0, 2.0


def f(x):
    return math.log(x) / (1 + x)


def runge(method, k, eps, n0=2, verbose=True):
    """Правило Рунге: подвоюємо n, доки |I_2n - I_n| / (2^k - 1) < eps.
    k - порядок точності формули (середніх прямокутників, трапецій: 2; Сімпсона: 4;
    лівих/правих прямокутників: 1). Повертає (n, I_2n, оцінка похибки)."""
    n = n0
    prev = method(n)
    if verbose:
        print(f"  n={n:4d}  I={prev:.8f}")
    while True:
        n *= 2
        cur = method(n)
        err = abs(cur - prev) / (2**k - 1)
        if verbose:
            print(f"  n={n:4d}  I={cur:.8f}  |I2n-In|/(2^{k}-1) = {err:.2e}")
        if err < eps:
            return n, cur, err
        prev = cur


def d2(x):
    """f''(x) = -1/(x^2(1+x)) - 2/(x(1+x)^2) + 2 ln x/(1+x)^3."""
    return (-1 / (x**2 * (1 + x)) - 2 / (x * (1 + x)**2)
            + 2 * math.log(x) / (1 + x)**3)


def d1(x):
    """f'(x) = 1/(x(1+x)) - ln x/(1+x)^2."""
    return 1 / (x * (1 + x)) - math.log(x) / (1 + x)**2


def d4(x):
    """f''''(x) за формулою Лейбніца для u = ln x, v = 1/(1+x)."""
    def u(k):  # k-та похідна ln x, k >= 1
        return (-1)**(k - 1) * math.factorial(k - 1) / x**k

    def v(m):  # m-та похідна 1/(1+x)
        return (-1)**m * math.factorial(m) / (1 + x)**(m + 1)

    total = math.log(x) * v(4)
    for k in range(1, 5):
        total += math.comb(4, k) * u(k) * v(4 - k)
    return total


def max_abs(g, steps=20000):
    """max |g| на [A, B] (перебір по густій сітці)."""
    return max(abs(g(A + (B - A) * i / steps)) for i in range(steps + 1))


if __name__ == "__main__":
    print("M1 = max|f'|    =", round(max_abs(d1), 6))
    print("M2 = max|f''|   =", round(max_abs(d2), 6), " (f''(1) =", d2(1.0), ")")
    print("M4 = max|f''''| =", round(max_abs(d4), 6), " (f''''(1) =", d4(1.0), ")")
