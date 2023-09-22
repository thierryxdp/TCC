def qtd_divisores(n):
    divisores = 1
    for divisor in range(1,n+1):
        if n&divisor == 0:
            divisores = divisores + 1
    return divisores