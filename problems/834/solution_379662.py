def media_matriz(matriz):
    """Função que calcula a media de todos os números pertencentes a uma matriz.
    list -> int."""
    contador = 0
    somatorio = 0
    for i in range(len(matriz)):
        for n in range(len(matriz[0])):
            contador += 1
            somatorio += matriz[i][n]
    
    media = somatorio/contador
    return round(media,2)