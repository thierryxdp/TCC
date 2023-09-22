def media_matriz (matriz):
    '''função que dada uma matriz de inteiros, não vazia, retorna a média de todos os númeors da matriz;
    list->list'''
    a =0
    lin = len(matriz)
    col = len(matriz[0])
    media = 0
    for elem in matriz:
        a+=sum(elem)
    media+=a/(lin*col)
    return media