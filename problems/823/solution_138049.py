def faltante(L):
    '''Esta função identifica o inteiro faltante de uma lista.
list->int'''
    i=0
    faltante=0
    list.sort(L)
    while i<len(L):
        if L[i]!=i+1:
            faltante=L[i]-2
        i=i+1
    return faltante