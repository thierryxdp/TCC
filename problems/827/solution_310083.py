def qtd_divisores(numero):
    qtd = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            qtd += 1
    return qtd