def qtd_divisores(n):
    divisores = []
    for x in range(n):
        if (n % x) == 0:
            list.append(divisores, x)
    return len(divisores)