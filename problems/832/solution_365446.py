def eh_quadrada(matriz):
    '''verifica se uma matriz é quadrada ou não
    list --> bool'''
    l= 0
    c= 0
    for x in matriz:
        l += 1
        c = len(x)
    return l == c