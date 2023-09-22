def qtd_divisores(numero):
    qtd = 0
    for x in range (1, numero + 1):
        if numero % x == 0:
            qtd = qtd + 1
    return qtd