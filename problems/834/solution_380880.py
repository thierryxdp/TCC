def media_matriz(matriz):
        i = 0
    soma = 0
    quantidade = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            soma += matriz[i][j]
            quantidade += 1
            j += 1
        i += 1
    media = soma / quantidade
    return round(media,2)