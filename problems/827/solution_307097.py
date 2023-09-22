def qtd_divisores(numero):
    divisores = []
    for i in range(1,numero):
        if numero%i == 0:
            divisores = divisores+[i,]
    return len(divisores)