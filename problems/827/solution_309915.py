qtd_divisores(n):
    divisores = 0
    for e in range(0,n + 1):
        if (n % e == 0):
            return divisores = divisores + 1
    return divisores