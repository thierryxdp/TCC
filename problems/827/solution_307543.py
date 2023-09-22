def qtd_divisores(numero):
    divisores = []
    for d in range(numero):
        if d%numero == 0:
            divisores = divisores + d
    return sum(divisores)