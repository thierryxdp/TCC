def repetidos (lista):
    """ """
    i=0
    x=0
    while i<len(lista):
        lista[x]=lista[x+1]
        i=i+1
    return i