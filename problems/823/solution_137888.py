def faltante(L):
    ''' '''
    x=[]
    list.sort(L)
    lista2=list(range(1,len(L)+2))
    x=int(list(set(lista2)-set(L)))
    return x