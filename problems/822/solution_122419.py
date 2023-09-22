def repetidos (lista):
    """ """
    i=0
    x=0
    while i-1<len(lista):
        lista[i]=lista[i-1]
        i=i+1
    return i