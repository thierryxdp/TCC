def repetidos (lista):
    """ """
    i=0
    x=0
    while i<len(lista)-1:
        lista[i]=lista[i-1]
        i=i+1
    return i