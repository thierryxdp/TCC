def media_matriz(matriz):
    """Retorna a media de todos os numeros
    que estao na matriz, arredondando o valor
    para duas casas decimais.
    list - float"""
    valor = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            tamanho = len(matriz) * len(matriz[i])
            valor += matriz[i][j]
    media = valor / tamanho
    return round(media,2)