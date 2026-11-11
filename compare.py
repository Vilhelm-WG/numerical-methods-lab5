"""Завдання 1.4 — порівняння результатів (відповідальний: Вільгельм)."""
import newton, stirling, simple


def main():
    results = {}
    for mod in (newton, stirling, simple):
        results.update(mod.solve())

    print(f"{'Завдання':34s}{'f\'':>12s}{'f\'\'':>12s}")
    for name, (f1, f2) in results.items():
        print(f"{name:34s}{f1:12.4f}{f2:12.4f}")

    # Порівняння в спільній точці x = 1.598 (Стірлінг vs прості формули)
    s1, s2 = stirling.stirling(1.598)
    c1, c2 = simple.central(1.598)
    print("\nx = 1.598: Стірлінг vs центральні різниці")
    print(f"  Δf'  = {abs(s1 - c1):.4f}")
    print(f"  Δf'' = {abs(s2 - c2):.4f}")


if __name__ == "__main__":
    main()
