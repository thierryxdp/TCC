def media_matriz(matriz:list)->float:
    """dada uma matriz de números inteiros não vazia, retorna média com duas casas decimais de precisão"""
    div=0
    somanums=0
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            somanums+=matriz[i][j]
            div+=1
    media=somanums/div
    return somanums