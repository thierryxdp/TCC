def qtd_divisores(numero):
    contador = 0
    for i in range(0,numero+1):
        if numero//i == 0:
            contador += 1
    return contador