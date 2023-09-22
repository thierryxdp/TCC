def qtd_divisores(numero):
    divisores = 0
    for i in range(0, numero):
        if numero % i == 0:
            divisores += 1 
    return divisores