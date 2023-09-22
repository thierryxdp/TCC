def faltante(L):
    '''Retorna o numero que esta faltando na sequencia da lista
    list->int'''
    list.sort(L)
    i=0
    while i<len(L):
        if L[i]-L[i-1]!=1:
            x=L[i]-1
        i+=1
    if x==0:
        x=L[i-1]+1
    return x