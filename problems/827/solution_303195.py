def qtd_divisores(numero):
    divisores = 0
    for i in range(numero):
        if i%numero ==0:
            divisores=divisores+ i
    return divisores+1