def melhor_volta(matriz6x10):
    '''list->tuple.'''
    lin = 6
    col = 10
    t = ()
    for i in range(0,6):
        for c in range(0,10):
            if matriz6x10[i][c] == min(min(matriz6x10)):
                tempo = (matriz6x10[i][c])
                corredor = (i+1)
                volta = (c + 1)
                
    return (tempo, corredor, volta)