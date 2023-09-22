def faltante(L):
    ''' '''
    lista_org=list.sort(L)
    i=0
    while i<len(L):
        if lista_org[i]-lista_org[i-1]!=1:
            x=lista_org[i]-1
        i+=1
    return x