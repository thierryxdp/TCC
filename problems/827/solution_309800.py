def qtd_divisores(n):
    divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            divisores += 1
    return divisores