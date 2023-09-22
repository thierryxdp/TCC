def eh_quadrada(M):
    '''Identifica se uma matriz é quadrada;
    list -> bool'''
    a = bool
    for i in range(len(M)):
        for j in range(len(M[i])):
            if range(len(M)) == range(len(M[i])):
                a = True
            elif len(M) == 0:
                a = True
            else:
                a = False
    return a