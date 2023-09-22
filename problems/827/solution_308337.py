def qtd_divisores(n):
    divisores = []
    d = 1
    for x in range(n):
        if (n % d) == 0:
            list.append(divisores, x)
        d += 1
    return len(divisores)