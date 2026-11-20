"""Порівняння результатів Задачі 2 (відповідальний: Вільгельм)."""
import rectangles, trapezoid, simpson
from simpson import simpson as simpson_n

REF = simpson_n(2000)  # еталон для порівняння (дуже дрібне розбиття)


def main():
    print(f"Еталон (Сімпсон, n = 2000): {REF:.8f}\n")
    print(f"{'Метод':34s}{'n':>5s}{'I':>14s}{'|I - еталон|':>16s}")
    for mod in (rectangles, trapezoid, simpson):
        for name, (n, val, err) in mod.solve().items():
            print(f"{name:34s}{n:5d}{val:14.8f}{abs(val - REF):16.2e}")

    print("\n2.2 Апріорні оцінки та фактична похибка при заданому розбитті")
    mid, _, m2, _ = rectangles.a_priori(5)
    tr, _ = trapezoid.a_priori(5)
    sp, m4 = simpson.a_priori(6)
    rows = [("Середні прямокутники, n=5", mid, abs(rectangles.rect_mid(5) - REF)),
            ("Трапеції, n=5", tr, abs(trapezoid.trap(5) - REF)),
            ("Сімпсон, n=6", sp, abs(simpson_n(6) - REF))]
    print(f"{'Метод':34s}{'апріорна оцінка':>18s}{'фактична':>14s}")
    for name, est, act in rows:
        print(f"{name:34s}{est:18.3e}{act:14.3e}")


if __name__ == "__main__":
    main()
