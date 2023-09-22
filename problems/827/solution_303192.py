def qnt_divisores(numero):
    divisores = 0
    for i in range(numero):
        if numero%i ==0:
            divisores=divisores+ i
    return divisores