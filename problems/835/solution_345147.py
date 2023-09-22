def melhor_volta(matriz):
    '''recebe uma matriz com tempos e retorna uma tupla com a melhor volta da prova, qual tempo e em que volta
lista(lista) -> tupla'''
    melhoresTempos = []
    melhorTempo = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == min(matriz[i]):
                pos = list.index(matriz[i], j) + 1
                tempo = j
                corredor = list.index(matriz, matriz[i]) + 1
                melhores = [corredor, tempo, pos]
        		list.append(melhoresTempos, melhores)
    for k in range(len(melhoresTempos)):
        for r in range(len(melhoresTempos[0])):
            if r == min(melhoresTempos[k][1]):
                return melhoresTempos[k]