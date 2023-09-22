def qtd_divisores(numero):
    divisores = []
    for i in range(numero):
        if numero % i == 0:
            divisores.append(i)
    return len(divisores)