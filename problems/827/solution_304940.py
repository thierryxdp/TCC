def qtd_divisores(n):
    divisores = 0
    for i in range(0, n):
        if (n%i) == 0:
            divisores = divisores + 1
    return divisores