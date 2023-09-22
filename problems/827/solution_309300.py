def qtd_divisores(numero):
    divisores=0
    for i in range(0, numero+1):
        if numero%i == 0:
            divisores= i +1
    return divisores