def qtd_divisores(numero):
    divisores = []
    for d in range(1, numero+1):
        if numero%d == 0:
            list.append(divisores, 1)
    return sum(divisores)