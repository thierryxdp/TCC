def faltante(lista):
    c=1
    t=0
    k=sorted(lista)
    l=[]
    while c<len(lista)+1:
        if k[t]!=c:
            return c
        c=c+1
        t=t+1
    return c