def media_matriz(matriz):
    """funcao que dada uma matriz retorna a media de todos os numeros da matriz;
    list->float"""
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    return round(soma/(len(matriz)*len(matriz[0])),2)