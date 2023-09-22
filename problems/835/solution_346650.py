def melhor_volta(matriz):
    '''uma função que analisa qual corredor em um corrida de kart fez a melhor volta no menor tempo,
    retornando uma tupla contendo o corredor, o tempo e qual volta...'''
    tempos = []
    melhores = []
    for a in range(len(matriz)):
        melhores.append((a+1,min(matriz[a]),matriz[a].index(min(matriz[a]))+1))
        tempos.append(min(matriz[a]))
    melhor = tempos.index(min(tempos))
    return (melhores[melhor])