def eh_quadrada(M):
    '''Identifica se uma matriz é quadrada;
    list -> bool'''
    a = 1
    for i in range(len(M)):
        for j in range(len(M[0])):
            if len(M) == len(M[0]):
                a = a
            else:
                a = a - 1
    return bool(a)