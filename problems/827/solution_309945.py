def qtd_divisores(numero):
    c = 0
    for i in range (numero + 1):
        if numero % i == 0:
            c += 1
    return c