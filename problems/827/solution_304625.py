qtd_divisores(n):
    qtd = 0
    for div in range(1,n):
        if (n % div == 0):
            qtd += 1
    return qtd