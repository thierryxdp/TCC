def qtd_divisores(numero):
    total = 0
    for i in range(1, int(numero/2) + 1):
        if numero%i==0:
            total = total + 1
    return total