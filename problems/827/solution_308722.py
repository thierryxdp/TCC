def qtd_divisores(n):
    qtd = 0
    for i in range(1, n + 1):
        if n % 1 == 0:
            qtd += 1
    return qtd