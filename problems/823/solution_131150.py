def faltante(L):
    i=0
    N=len(lista)
    lista=[]
    while i<len(L):
        if lista[0:N]in L[0:N]:
            i=i+1
    return lista-L