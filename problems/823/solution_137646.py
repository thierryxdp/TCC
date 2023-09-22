def faltante(L):
    '''função que dada uma lista retorna o numero x que pertence ao intervalo [1,N]
    mas não pertence a lista; list->int'''
    list.sort(L)
    i=0
    while i<len(L):
        if len(L)==1 and 1<L[0]<3:
            x=L[0]-1
            return x
        if L[i]-1 not in L and L[i]>1:
            x=L[i]-1
            return x
        i=i+1