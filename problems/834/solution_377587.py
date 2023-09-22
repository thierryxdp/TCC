def media_matriz(matriz):
    """Função que dada a matriz da entrada retorna a media de todos os numeros da matriz; int-> float"""
    matriz_r=list()
    c=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz_r=sum([i][j])/len(matriz)