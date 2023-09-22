def media_matriz(matriz):
    '''Função que dada uma matriz de numeros inteiros nao vazia, retorna a média de todos os numeros da matriz com exatamente duas casas demais.
    list(list) -> int'''
    x = 0
    for y in range(len(matriz)):
        x = x+sum(matriz[y])
    media = x/(len(matriz)*len(matriz[0]))
    return round(media,2)