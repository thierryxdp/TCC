def qtd_divisores(numero):
    divisores=0
    for num in range(1, int(numero) + 1):
        if numero%num == 0:
            divisores=divisores+1
    return divisores