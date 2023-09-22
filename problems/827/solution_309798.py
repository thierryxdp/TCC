def qtd_divisores(m):
    "funcao que conta quantos divisores um numero tem"
    divisores = 0
    i = 1
    while i <= m:
        if n % i == 0:
            divisores += 1
        i += 1
    return divisores