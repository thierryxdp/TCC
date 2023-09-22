def media_matriz(n):
    '''Calcula a media de uma matriz(n),desde que seja uma matriz de inteiros não vazia. list(list)->float'''
    i=0
    p=0
    while i<len(n):
        p=sum(n[i])+p
        i=i+1
    return round(p/(len(n[0])*len(n)),2)