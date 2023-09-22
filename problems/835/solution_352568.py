def melhor_volta(matriz):
    ''' uma função que analisa uma corrida de kart e retorna uma tupla
    contendo o corredor, o tempo da melhor volta e qual foi'''
    tempos = []
    melhores = []
    for a in range (len(matriz)):
        melhores.append((a+1,min(matriz[a],matriz[a].index(min(matriz[a]))+1))
        tempos.append(min(matriz[a])
    melhor = tempo.index(min(tempos))
    return (melhores[melhor])