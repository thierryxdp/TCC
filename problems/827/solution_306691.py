def qtd_divisores(numero):
    '''retorna quantos divisores o numero inserido tem.
    int -> int'''
    divisores = []
    for i in range(1, numero):
        if numero / i == numero // 1:
            divisores = divisores.append(i)
    return len(divisores)