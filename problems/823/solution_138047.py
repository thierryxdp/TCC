def faltante(L):
    '''Esta função identifica o inteiro faltante de uma lista.
list->int'''
    i=0
    while i<len(L):
        L.sort()
        if L[i]!=i+1:
            faltante=i+1
        i=i+1
    return faltante