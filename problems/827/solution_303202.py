def qtd_divisores(numero):
    divisores = 0
    for i in range(1,numero):
        if numero%i ==0:
            divisores=divisores+ i
    return divisores