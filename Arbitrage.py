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

table = {
    0: "tokenA",
    1: "tokenB",
    2: "tokenC",
    3: "tokenD",
    4: "tokenE"
}

path = []

for i in range(0, 5):
    if i == 1: continue
    delta_x = 5
    if("tokenB", table.get(i)) in liquidity:
        tokenB_balance = liquidity[("tokenB", table.get(i))][0]
        tokeni_balance = liquidity[("tokenB", table.get(i))][1]
    else:
        tokenB_balance = liquidity[(table.get(i), "tokenB")][1]
        tokeni_balance = liquidity[(table.get(i), "tokenB")][0]
    delta_1y = (997 * delta_x * tokeni_balance) / (1000 * tokenB_balance + 997 * delta_x)

    for j in range(0, 5):
        if j == 1 or j == i: continue
        delta_x = delta_1y
        if(table.get(i), table.get(j)) in liquidity:
            tokeni_balance = liquidity[table.get(i), table.get(j)][0]
            tokenj_balance = liquidity[table.get(i), table.get(j)][1]
        else:
            tokeni_balance = liquidity[table.get(j), table.get(i)][1]
            tokenj_balance = liquidity[table.get(j), table.get(i)][0]
        delta_2y = (997 * delta_x * tokenj_balance) / (1000 * tokeni_balance + 997 * delta_x)
        
        delta_x = delta_2y
        if(table.get(j), "tokenB") in liquidity:
            tokenj_balance = liquidity[table.get(j), "tokenB"][0]
            tokenB_balance = liquidity[table.get(j), "tokenB"][1]
        else:
            tokenj_balance = liquidity["tokenB", table.get(j)][1]
            tokenB_balance = liquidity["tokenB", table.get(j)][0]
        delta_3y = (997 * delta_x * tokenB_balance) / (1000 * tokenj_balance + 997 * delta_x)

        temp_path = ["tokenB", table.get(i), table.get(j), "tokenB", delta_3y]
        path.append(temp_path)
        """
        print(f"path: tokenB->{table.get(i)}->{table.get(j)}->tokenB, tokenB balance={delta_3y:.6f}")
        print(f"tokenB->{table.get(i)}, amountIn=5, amountOut={delta_1y}")
        print(f"{table.get(i)}->{table.get(j)}, amountIn={delta_1y}, amountOut={delta_2y}")
        print(f"{table.get(j)}->tokenB, amountIn={delta_2y}, amountOut={delta_3y}")
        print()
        """
for i in range(0, 5):
    if i == 1: continue
    delta_x = 5
    if("tokenB", table.get(i)) in liquidity:
        tokenB_balance = liquidity[("tokenB", table.get(i))][0]
        tokeni_balance = liquidity[("tokenB", table.get(i))][1]
    else:
        tokenB_balance = liquidity[(table.get(i), "tokenB")][1]
        tokeni_balance = liquidity[(table.get(i), "tokenB")][0]
    delta_1y = (997 * delta_x * tokeni_balance) / (1000 * tokenB_balance + 997 * delta_x)

    for j in range(0, 5):
        if j == 1 or j == i: continue
        delta_x = delta_1y
        if(table.get(i), table.get(j)) in liquidity:
            tokeni_balance = liquidity[table.get(i), table.get(j)][0]
            tokenj_balance = liquidity[table.get(i), table.get(j)][1]
        else:
            tokeni_balance = liquidity[table.get(j), table.get(i)][1]
            tokenj_balance = liquidity[table.get(j), table.get(i)][0]
        delta_2y = (997 * delta_x * tokenj_balance) / (1000 * tokeni_balance + 997 * delta_x)

        for k in range(0, 5):
            if k == 1 or k == i or k == j: continue
            delta_x = delta_2y
            if(table.get(j), table.get(k)) in liquidity:
                tokenj_balance = liquidity[table.get(j), table.get(k)][0]
                tokenk_balance = liquidity[table.get(j), table.get(k)][1]
            else:
                tokenj_balance = liquidity[table.get(k), table.get(j)][1]
                tokenk_balance = liquidity[table.get(k), table.get(j)][0]
            delta_3y = (997 * delta_x * tokenk_balance) / (1000 * tokenj_balance + 997 * delta_x)
                    
            delta_x = delta_3y
            if(table.get(k), "tokenB") in liquidity:
                tokenk_balance = liquidity[table.get(k), "tokenB"][0]
                tokenB_balance = liquidity[table.get(k), "tokenB"][1]
            else:
                tokenk_balance = liquidity["tokenB", table.get(k)][1]
                tokenB_balance = liquidity["tokenB", table.get(k)][0]
            delta_4y = (997 * delta_x * tokenB_balance) / (1000 * tokenk_balance + 997 * delta_x)

            temp_path = ["tokenB", table.get(i), table.get(j), table.get(k), "tokenB", delta_4y]
            path.append(temp_path)
            """
            print(f"path: tokenB->{table.get(i)}->{table.get(j)}->{table.get(k)}->tokenB, tokenB balance={delta_4y:.6f}")
            print(f"tokenB->{table.get(i)}, amountIn=5, amountOut={delta_1y}")
            print(f"{table.get(i)}->{table.get(j)}, amountIn={delta_1y}, amountOut={delta_2y}")
            print(f"{table.get(j)}->{table.get(k)}, amountIn={delta_2y}, amountOut={delta_3y}")
            print(f"{table.get(k)}->tokenB, amountIn={delta_3y}, amountOut={delta_4y}")
            print()
            """
for i in range(0, 5):
    if i == 1: continue
    delta_x = 5
    if("tokenB", table.get(i)) in liquidity:
        tokenB_balance = liquidity[("tokenB", table.get(i))][0]
        tokeni_balance = liquidity[("tokenB", table.get(i))][1]
    else:
        tokenB_balance = liquidity[(table.get(i), "tokenB")][1]
        tokeni_balance = liquidity[(table.get(i), "tokenB")][0]
    delta_1y = (997 * delta_x * tokeni_balance) / (1000 * tokenB_balance + 997 * delta_x)

    for j in range(0, 5):
        if j == 1 or j == i: continue
        delta_x = delta_1y
        if(table.get(i), table.get(j)) in liquidity:
            tokeni_balance = liquidity[table.get(i), table.get(j)][0]
            tokenj_balance = liquidity[table.get(i), table.get(j)][1]
        else:
            tokeni_balance = liquidity[table.get(j), table.get(i)][1]
            tokenj_balance = liquidity[table.get(j), table.get(i)][0]
        delta_2y = (997 * delta_x * tokenj_balance) / (1000 * tokeni_balance + 997 * delta_x)

        for k in range(0, 5):
            if k == 1 or k == i or k == j: continue
            delta_x = delta_2y
            if(table.get(j), table.get(k)) in liquidity:
                tokenj_balance = liquidity[table.get(j), table.get(k)][0]
                tokenk_balance = liquidity[table.get(j), table.get(k)][1]
            else:
                tokenj_balance = liquidity[table.get(k), table.get(j)][1]
                tokenk_balance = liquidity[table.get(k), table.get(j)][0]
            delta_3y = (997 * delta_x * tokenk_balance) / (1000 * tokenj_balance + 997 * delta_x)

            for l in range(0, 5):
                if l == 1 or l == i or l == j or l == k: continue
                delta_x = delta_3y
                if(table.get(k), table.get(l)) in liquidity:
                    tokenk_balance = liquidity[table.get(k), table.get(l)][0]
                    tokenl_balance = liquidity[table.get(k), table.get(l)][1]
                else:
                    tokenk_balance = liquidity[table.get(l), table.get(k)][1]
                    tokenl_balance = liquidity[table.get(l), table.get(k)][0]
                delta_4y = (997 * delta_x * tokenl_balance) / (1000 * tokenk_balance + 997 * delta_x)
                    
                delta_x = delta_4y
                if(table.get(l), "tokenB") in liquidity:
                    tokenl_balance = liquidity[table.get(l), "tokenB"][0]
                    tokenB_balance = liquidity[table.get(l), "tokenB"][1]
                else:
                    tokenl_balance = liquidity["tokenB", table.get(l)][1]
                    tokenB_balance = liquidity["tokenB", table.get(l)][0]
                delta_5y = (997 * delta_x * tokenB_balance) / (1000 * tokenl_balance + 997 * delta_x)

                temp_path = ["tokenB", table.get(i), table.get(j), table.get(k), table.get(l), "tokenB", delta_5y]
                path.append(temp_path)
                """
                print(f"path: tokenB->{table.get(i)}->{table.get(j)}->{table.get(k)}->{table.get(l)}->tokenB, tokenB balance={delta_5y:.6f}")
                print(f"tokenB->{table.get(i)}, amountIn=5, amountOut={delta_1y}")
                print(f"{table.get(i)}->{table.get(j)}, amountIn={delta_1y}, amountOut={delta_2y}")
                print(f"{table.get(j)}->{table.get(k)}, amountIn={delta_2y}, amountOut={delta_3y}")
                print(f"{table.get(k)}->{table.get(l)}, amountIn={delta_3y}, amountOut={delta_4y}")
                print(f"{table.get(l)}->tokenB, amountIn={delta_4y}, amountOut={delta_5y}")
                print()
                """

path = sorted(path, key=lambda x: x[-1], reverse=True)
print(f"path: {'->'.join(path[0][:-1])}, tokenB balance={path[0][-1]:.6f}")