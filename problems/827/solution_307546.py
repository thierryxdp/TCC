def qtd_divisores(numero):
    divisores = []
    for d in range(numero+1):
        if d%numero == 0:
            list.append(divisores, d)
    return sum(divisores)