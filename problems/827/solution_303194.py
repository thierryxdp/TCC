def qtd_divisores(numero):
    divisores = 0
    for i in range(numero+1):
        if numero%i ==0:
            divisores=divisores+ i
    return divisores