def qtd_divisores(numero):
    divisores = []
    for d in range(numero+1):
        if numero%d == 0:
            list.append(divisores, d)
    return sum(divisores)