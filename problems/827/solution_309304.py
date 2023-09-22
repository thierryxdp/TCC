def qtd_divisores(numero):
    divisores=0
    for i in range(1, numero//2):
        if numero%i == 0:
            divisores= i
    return divisores