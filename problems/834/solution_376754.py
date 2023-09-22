def media_matriz(matriz):
    """Funcao que calcula a media dos numeros da matriz. List-->Int"""
    media = 0
    numero = 0
    quantidade = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            numero += matriz[i][j]
            quantidade += 1
    media = numero/quantidade
    return round(media,2)