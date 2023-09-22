def melhor_volta(matriz6x10):
    '''list->tuple.'''
    lin = 6
    col = 10
    for i in range(0,6):
        for c in range(0,10):
            if matriz6x10[i][c] == min(matriz6x10):
                t = t + (i) + (min(matriz6x10)) + (c) 
    return t