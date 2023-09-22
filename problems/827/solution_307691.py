def qtd_divisores(numero):
    i = 0
    for x in range(1, numero + 1):
        if numero % x == 0:
            i = i + 1
    return i