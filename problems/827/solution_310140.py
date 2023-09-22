def qtd_divisores(n):
    divisores = 0
    for e in range(1, n+1):
        if (n%e==0):
            divisores = divisores + 1
    return divisores