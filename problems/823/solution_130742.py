def faltante(lista):
    c=0
    p=[]
    d=0
    while c<len(lista):
        if c in lista :
            d=d+1
        else:
            return c
        c=c+1