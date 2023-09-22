def qtd_divisores(numero):
    divisores = []
    for i in range(1,numero+1):
        if numero%i == 0:
            list.append(divisores, i)
    return len(divisores)