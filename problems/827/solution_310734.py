def qtd_divisores(x):
    divisor = 1
    divisores = 0
    while divisor < x:
        if x%divisor == 0:
            divisores += 1
            divisor += 1
    return divisores