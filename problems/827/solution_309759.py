def qtd_divisores(n):
    divisores = 0
    for divisor in range(1,n+2):
        if n&divisor == 0:
            divisores = divisores + 1
    return divisores