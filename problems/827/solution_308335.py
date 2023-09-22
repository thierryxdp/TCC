def qtd_divisores(n):
    divisores = []
    d = 0
    for x in range(n):
        if (n % d) in range(n):
            list.append(divisores, x)
        d += 1
    return len(divisores)