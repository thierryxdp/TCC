def qtd_divisores(numero):
    '''
    '''
    divisores = 0
    for n in range(numero):
        if numero%n == 0:
            divisores = divisores + 1
    return divisores