def qtd_divisores(numero):
    '''retorna quantos divisores o numero inserido tem.
    int -> int'''
    divisores = []
    for i in range(numero):
        if numero / i == numero // 1:
            divisores.append(i)
    return len(divisores)