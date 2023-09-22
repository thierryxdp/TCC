def qtd_divisores(n):
    divisores = []
    d = 1
    for x in range(n):
        if (n % d) in range(n):
            list.append(divisores, x)
        d += 1
    return len(divisores)