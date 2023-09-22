def faltante(lista):
    i=0
    N=len(lista)
    x=0
    v=[]
    while N>0:
        v=v+N
        N=N-1
    while i<len(lista):
        if lista[i] in v==True:
            i=i+1
        else:
            x=x+lista[i]
            i=i+1
    return x