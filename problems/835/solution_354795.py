def melhor_volta(matriz6x10):
    '''list->tuple.'''
    lin = 6
    col = 10
    t = []
    for i in range(0,6):
        for c in range(0,10):
            if matriz6x10[i][c] == min(matriz6x10[i]):
                list.append(t,matriz6x10[i][c])
                tempo = min(t)
                if matriz6x10[i][c] == tempo:
                    corredor = list.index(matriz6x10, matriz6x10[i]) + 1
                    volta = list.index(matriz6x10[i],matriz6x10[i][c]) + 1
        
    return (tempo, corredor, volta)