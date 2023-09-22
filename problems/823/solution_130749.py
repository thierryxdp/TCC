def faltante(lista):
    c=1
    k=sorted(lista)
    l=[]
    while c<len(lista):
        if c not in k:
            return c
        if c==c[-1]:
            return c+1
        c=c+1
        
    return c