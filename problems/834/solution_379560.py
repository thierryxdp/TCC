def media_matriz(matriz):
    """ retorna a media de todos os numeros da matriz
    com duas casas deciamis
    list -> float"""
    soma = 0
    quant = 0
    for i in range(len(matriz)):
        quant += len(matriz[i])
        soma =+ sum(matriz[i])
        media = soma / quant
        media = round(media, 2)
    return media