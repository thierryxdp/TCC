def faltante (lista):
    """ """
    i=0
    list.sort(lista)
    while i< len(lista)+1:
        if lista[i]==i+1:
            return i+1
        
        else:
            return 0
        i+=1