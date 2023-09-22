def qtd_divisores(numero):
    '''Conta quantos divisores o número tem.
    int -> int'''
    qt = []
    for i in range(0,numero):
        if numero % i == 0:
        	qt += [i]
    return len(qt)