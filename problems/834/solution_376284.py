def media_matriz(m):
    """ Funçao que um numero inteiros, retorna a media de todos os numeros
    list-. float"""
    total=0
    quantidade=0
    media=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            total = total + m[i][j]
            quantidade= quantidade + 1
    media= toal/quantidade
    return round(media, 2)