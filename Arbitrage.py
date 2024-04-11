liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

exchange_rates = [
    [1, 10/17, 7/11, 9/15, 5/21],
    [17/10, 1, 4/36, 6/13, 3/25],
    [11/7, 36/4, 1, 12/30, 8/10],
    [15/9, 13/6, 30/12, 1, 25/60],
    [5/21, 25/3, 10/8, 60/25, 1]
]

table = {
    0: "tokenA",
    1: "tokenB",
    2: "tokenC",
    3: "tokenD",
    4: "tokenE"
}

path = []

for i in range(0, 5):
    for j in range(0, 5):
        if i == j:
            continue
        for k in range(0, 5):
            if k == i or k == j:
                continue
            else:
                value = exchange_rates[i][k] * exchange_rates[k][j] * exchange_rates[j][i]
                temp_path = [i, k, j, i, value]
                path.append(temp_path)

for i in range(0, 5):
    for j in range(0, 5):
        if i == j:
            continue
        for k in range(0, 5):
            if k == i or k == j:
                continue
            for l in range(0, 5):
                if l == i or l == j or l == k:
                    continue
                else:
                    value = exchange_rates[i][k] * exchange_rates[k][l] * exchange_rates[l][j] * exchange_rates[j][i]
                    temp_path = [i, k, l, j, i, value]
                    path.append(temp_path)

for i in range(0, 5):
    for j in range(0, 5):
        if i == j:
            continue
        for k in range(0, 5):
            if k == i or k == j:
                continue
            for l in range(0, 5):
                if l == i or l == j or l == k:
                    continue
                for m in range(0, 5):
                    if m == i or m == j or m == k or m == l:
                        continue
                    else:
                        value = exchange_rates[i][k] * exchange_rates[k][l] * exchange_rates[l][m] * exchange_rates[m][j] * exchange_rates[j][i]
                        temp_path = [i, k, l, m, j, i, value]
                        path.append(temp_path)

path = sorted(path, key=lambda x: x[-1], reverse=True)

tokens = [table[i] for i in path[0][:-1]]
token_path = "->".join(tokens)
balance = path[0][-1]
print(f"path: {token_path}, balance={balance}")