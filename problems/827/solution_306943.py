def qtd_divisores(numero):
    '''
    '''
    divisores = 0
    for n in range(1,numero):
        if numero%n == 0:
            divisores = divisores + 1
    return divisores