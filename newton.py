import numpy as np

def solve_newton_derivatives():
    # Вхідні дані для варіанта 3
    x = np.array([0.248, 0.923, 1.598, 2.273, 2.948])
    y = np.array([-3.642, 0.802, 0.841, 0.513, 0.328])
    h = 0.675
    n = len(y)

    # Побудова таблиці скінченних різниць
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i+1, j-1] - diff_table[i, j-1]

    print("=== ПУНКТ 1.1 а) Точка x = 0.248 (Перша формула Ньютона — вперед) ===")
    x_a = 0.248
    x0 = x[0]
    q_a = (x_a - x0) / h  # дорівнює 0, оскільки збігається з першим вузлом

    # Різниці з першого рядка таблиці
    Dy0   = diff_table[0, 1]
    D2y0  = diff_table[0, 2]
    D3y0  = diff_table[0, 3]
    D4y0  = diff_table[0, 4]

    # Формули для першої та другої похідних (вперед)
    f_prime_a = (1 / h) * (
        Dy0 +
        ((2 * q_a - 1) / 2) * D2y0 +
        ((3 * q_a**2 - 6 * q_a + 2) / 6) * D3y0 +
        ((4 * q_a**3 - 18 * q_a**2 + 22 * q_a - 6) / 24) * D4y0
    )

    f_double_prime_a = (1 / h**2) * (
        D2y0 +
        (q_a - 1) * D3y0 +
        ((6 * q_a**2 - 18 * q_a + 11) / 12) * D4y0
    )

    print(f"q = {q_a}")
    print(f"f'(0.248)  = {f_prime_a:.4f}")
    print(f"f''(0.248) = {f_double_prime_a:.4f}\n")

    print("=== ПУНКТ 1.1 б) Точка x = 2.8 (Друга формула Ньютона — назад) ===")
    x_b = 2.8
    x_last = x[-1]  # x4 = 2.948
    q_b = (x_b - x_last) / h

    # Різниці з кінця таблиці
    Dy_last   = diff_table[3, 1]
    D2y_last2 = diff_table[2, 2]
    D3y_last3 = diff_table[1, 3]
    D4y_last4 = diff_table[0, 4]

    # Формули для першої та другої похідних (назад)
    f_prime_b = (1 / h) * (
        Dy_last +
        ((2 * q_b + 1) / 2) * D2y_last2 +
        ((3 * q_b**2 + 6 * q_b + 2) / 6) * D3y_last3 +
        ((4 * q_b**3 + 18 * q_b**2 + 22 * q_b + 6) / 24) * D4y_last4
    )

    f_double_prime_b = (1 / h**2) * (
        D2y_last2 +
        (q_b + 1) * D3y_last3 +
        ((6 * q_b**2 + 18 * q_b + 11) / 12) * D4y_last4
    )

    print(f"q = {q_b:.5f}")
    print(f"f'(2.8)  = {f_prime_b:.4f}")
    print(f"f''(2.8) = {f_double_prime_b:.4f}")

if __name__ == "__main__":
    solve_newton_derivatives()
