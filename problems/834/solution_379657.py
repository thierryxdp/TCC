def media_matriz(matriz):
    """Dada uma matriz retorna a média dos números dela.
    list -> float"""
    soma=0
    for i in range(len(matriz)):
        for k in range(len(matriz[0])):
            soma+=matriz[i][k]
        tamanho = len(matriz)*len(matriz[0])
        media =soma/tamanho
    return round(media,2)