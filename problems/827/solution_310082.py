def qtd_divisores(numero):
    qtd = 1
    for i in range(1,numero):
        if numero % i == 0:
            qtd += 1
    return qtd