def media_matriz(matriz):
    'Dada uma matriz retorne a média de todos os números desta matriz. list(list)-->float'
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=soma+ matriz[i][j]
    media= soma/(len(matriz)*len(matriz[0]))
    return media