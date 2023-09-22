def melhor_volta(matriz):
    '''recebe uma matriz com tempos e retorna uma tupla com a melhor volta da prova, qual tempo e em que volta
lista(lista) -> tupla'''
    comparacao = []
    for i in range(len(matriz)):
        melhoresTempos = []
        for j in range(len(matriz[0])):
            if matriz[i][j] == min(matriz[i]):
                pos = str.index(matriz[i][j]) + 1
                numero = i - 1
                tempo = matriz[i][j]
                corredor = (numero, tempo, posicao)
                list.append(melhoresTempos, corredor)
        for r in range(len(melhoresTempos)):
            if r == min(melhoresTempos[i][1]):
                return melhoresTempos[i]