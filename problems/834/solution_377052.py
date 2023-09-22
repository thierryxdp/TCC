def media_matriz(matriz):
    '''Ao fornecer uma matriz não nula, retorna a média
    de todos os seus valores.

    list -> float'''
    M = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(M,matriz[i][j])
    return round((sum(M)/len(M)),2)