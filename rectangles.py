from data2 import A, B, d1, d2, f, max_abs, runge


def rect_mid(n: int, a: float = A, b: float = B) -> float:
    """Формула середніх прямокутників при розбитті [a, b] на n частин."""
    h = (b - a) / n
    total = sum(f(a + (i + 0.5) * h) for i in range(n))
    return h * total


def rect_left(n: int, a: float = A, b: float = B) -> float:
    """Формула лівих прямокутників при розбитті [a, b] на n частин."""
    h = (b - a) / n
    total = sum(f(a + i * h) for i in range(n))
    return h * total


def a_priori(n: int = 5, a: float = A, b: float = B):
    """Апріорна оцінка похибки при розбитті на n рівних частин."""
    m2 = max_abs(d2)
    m1 = max_abs(d1)
    mid_err = ((b - a) ** 3) * m2 / (24 * (n ** 2))
    left_err = ((b - a) ** 2) * m1 / (2 * n)
    return mid_err, left_err, m2, m1


def solve(eps: float = 1e-2):
    """Запуск обчислень за правилом Рунге для порівняльного скрипта."""
    print("=== 2.1 а) Середні прямокутники (k=2, правило Рунге) ===")
    n_mid, val_mid, err_mid = runge(lambda n: rect_mid(n), k=2, eps=eps, n0=2, verbose=True)

    return {
        "Прямокутники (середні)": (n_mid, val_mid, err_mid),
    }


def main():
    results = solve(eps=1e-2)
    n_mid, val_mid, err_mid = results["Прямокутники (середні)"]
    print(f"\nПідсумок 2.1 а) (середні): n={n_mid}, I={val_mid:.5f}, оцінка={err_mid:.2e}")

    print("\n=== Додатково: Ліві прямокутники (k=1, правило Рунге) ===")
    n_left, val_left, err_left = runge(lambda n: rect_left(n), k=1, eps=1e-2, n0=2, verbose=True)
    print(f"Підсумок (ліві): n={n_left}, I={val_left:.5f}, оцінка={err_left:.2e}")

    print("\n=== 2.2 Апріорна оцінка похибки (n = 5) ===")
    mid_err, left_err, m2, m1 = a_priori(n=5)
    print(f"Середні прямокутники: M2={m2:.6f}, |R| <= {mid_err:.2e} ({mid_err:.5f})")
    print(f"Ліві прямокутники:    M1={m1:.6f}, |R| <= {left_err:.2e} ({left_err:.5f})")


if __name__ == "__main__":
    main()