def faltante(lista):
    c=0
    p=[]
    while c<len(lista):
        if c not in lista :
            return c
        c=c+1