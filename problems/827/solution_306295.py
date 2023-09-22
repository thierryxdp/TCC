def qtd_divisores(n):
    numero_divisores = 0
    for numero in range(n):
        if n % 2 == 0:
            numero_divisores += n
    return numero_divisores