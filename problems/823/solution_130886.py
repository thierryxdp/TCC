def faltante (lista):
    """ """
    i=0
    list.sort(lista)
    while i< len(lista):
        if lista[i]==i+1:
                i+=1
        else:
            i=0