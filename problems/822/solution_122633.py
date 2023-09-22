def repetidos(lista):
    """ """
    i=0
    n=0
    while i<len(lista):
        if lista[i]==lista[i+1]:
            return n+1
        else:
            return n
        i+=1
    return n