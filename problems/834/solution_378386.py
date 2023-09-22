def media_matriz(matriz):
    """Dada uma matriz de inteiros, a função calcula
    a media de todos os números da matriz e o retorna.
    Parametros de Entrada: list
    Retorna: float"""

    elementos=0
    soma=0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma= soma+ matriz[i][j]
            elementos= elementos+1
            
    media= soma/elementos

    return round(media,2)