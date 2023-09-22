def faltante(lista):
    c=lista[0]
    l=[]
    while c<len(lista):
        if c not in lista:
            return c