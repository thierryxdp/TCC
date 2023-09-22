def media_matriz(matriz):
    """Função que calcula a media dos numeros da matriz. List-->Int"""
    media_matriz = 0
    numero = 0
    quantidade = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            numero += matriz[i][j]
            quantidade += 1
    media_matriz = numero/quantidade
    return round(media_matriz,2)