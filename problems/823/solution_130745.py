def faltante(lista):
    c=lista[0]
    k=sorted(lista)
    l=[]
    while c<len(lista):
        if c not in k:
            return c
        c=c+1
    return 55