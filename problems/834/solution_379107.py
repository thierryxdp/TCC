def media_matriz(m):
    '''Dada uma matriz de números inteiros e não vazia,
    Retorna a média de todos os números da matriz.
    list->float'''
    n=0
    a=0
    i=0
    for lista in m:
        a+=sum(m[i])
        n+=len(m[i])
        i+=1
    return round((a)/(n),2)