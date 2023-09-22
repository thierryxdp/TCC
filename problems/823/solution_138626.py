def faltante(lista):
    i=0
    N=len(lista)+1
    um=0
    v=[]
    while N>0:
        v=v+[N,]
        N=N-1   
    while i<len(v):
            if v[i] in lista:
                i=i+1
            else:
                um=um+v[i]
                i=i+1
    return um