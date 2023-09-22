media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, retorna com a
media de todos os números da matriz.
list -> float"""
    media=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            media.index(matriz[i][j])
    return round(sum(media)/len(media),2)