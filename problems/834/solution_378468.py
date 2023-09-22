def media_matriz(matriz):
    '''Dada uma matriz de números inteiros não vazia, retorna
    a média de todos os números da matriz (com duas casas
    decimais de precisão).
    list -> float'''
    media=sum(matriz)/(len(matriz)+((len(matriz))*(len(matriz[0]))))
    return round(media,2)