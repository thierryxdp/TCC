def faltante (lista):
    """ """
    i=0
    list.sort(lista)
    while i< len(lista)+2:
        if lista[i]!=i+1:
            return i+1
        i+=1
    return i