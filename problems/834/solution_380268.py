def media_matriz (matriz):
    '''função que dada uma matriz de inteiros, não vazia, retorna a média de todos os númeors da matriz;
    list->list'''
    a =[]
    n = len(matriz)
    for lin in matriz:
        a+=sum(lin)
    for soma in a:
        media=sum(a)/n
    return media