def melhor_volta(matriz):
    '''Retorna uma tupla contendo de quem foi a
    melhor volta, com qual tempo e em que volta
    list --> tuple'''
    tempos = ()
    for i in range(len(matriz)):
        for j in matriz[i]:
            tempos += (j)
    minimo = min(tempos)
    for i in range(matriz):
        for j in matriz[i]:
            if minimo == j:
                return (i, minimo, j)