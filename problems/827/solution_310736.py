def qtd_divisores(x):
    divisor = 1
    while divisor < x:
        if x%divisor == 0:
            divisores += 1
            divisor += 1
    return divisores