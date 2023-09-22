def melhor_volta(matriz):
    '''recebe uma matriz com tempos e retorna uma tupla com a melhor volta da prova, qual tempo e em que volta
lista(lista) -> tupla'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == min(range(len(matriz[0]))):
                pos = str.index(matriz[i], matriz[i][j]) + 1
                tempo = str.index(matriz[i])
                corredor = str.index(matriz, matriz[i]) + 1
            return (corredor, tempo, pos)