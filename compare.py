"""Завдання 1.4 — порівняння результатів (відповідальний: Вільгельм)."""
import sys

import newton
import simple
import stirling

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    results = {}
    for mod in (newton, stirling, simple):
        results.update(mod.solve())

    d1, d2 = "f'", "f''"  # без бекслешів в f-рядках (сумісно з Python < 3.12)
    print(f"{'Завдання':34s}{d1:>12s}{d2:>12s}")
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