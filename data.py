"""Спільні дані варіанту №3 (відповідальний: Вільгельм).
НЕ змінювати без погодження з TeamLead.
"""

X = [0.248, 0.923, 1.598, 2.273, 2.948]
Y = [-3.642, 0.802, 0.841, 0.513, 0.328]
H = round(X[1] - X[0], 10)  # крок сітки h = 0.675 (вузли рівновіддалені)


def diff_table(y=Y):
    """Таблиця скінченних різниць: table[k][i] = Δ^(k+1) y_i."""
    table = []
    prev = list(y)
    while len(prev) > 1:
        cur = [prev[i + 1] - prev[i] for i in range(len(prev) - 1)]
        table.append(cur)
        prev = cur
    return table


if __name__ == "__main__":
    print("h =", H)
    for k, row in enumerate(diff_table(), start=1):
        print(f"Δ^{k} y:", [round(v, 6) for v in row])
