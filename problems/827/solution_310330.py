def qtd_divisores(numero):
    contador = 0
    for i in range(numero):
        if numero//i == 0:
            contador += 1
    return contador