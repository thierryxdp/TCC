def faltante(lista):
    """ """
    i=0
    list.sort(lista)
    nova= len(lista)+1
    while i< nova:
        if nova[i]!= i+1:
            return i+1
        i=i+1
    return i