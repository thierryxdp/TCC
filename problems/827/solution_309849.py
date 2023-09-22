def qtd_divisores(numero):
    i = 0
    for c in range(1,numero+1):
        if (numero % c) == 0:
            i += 1
    return i