def repetidos (lista):
    """ """
    i=0
    x=0
    while i<len(lista):
        if x in  lista:
            lista[x]=lista[x+1]
        i=i+1
        else:
            i=i
    return i