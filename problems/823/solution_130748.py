def faltante(lista):
    c=1
    k=sorted(lista)
    l=[]
    while c<len(lista):
        if c not in k:
            return c
        c=c+1
    return c