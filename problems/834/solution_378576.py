def media_matriz(matriz):
    """dada uma matriz nao vazia, retorna a media de todos os numeros da matriz;
    lista->float."""
    soma=0
    div=len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
    return round(soma/div,2)