def media_matriz(matriz):
    '''Calcula a media de todos os numeros de uma matriz
    de numeros inteiros com duas casas de precisão;
    list(list) -> float'''
    numeros = []
    for i in matriz:
        for j in i:
           list.append(numeros,j)
    divisor = len(numeros)
    dividendo = sum(numeros)
    media = dividendo/divisor
    return round(media,2)