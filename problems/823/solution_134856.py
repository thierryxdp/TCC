def faltante(lista):
    """ """
    ct = 0
    ct1 = ct + 1
    lista1 = range(1, len(lista)+1)
    while ct < len(lista):
        ct = ct + 1 
        if lista[ct] == lista1[ct] and ct == len(lista)-1:
            return lista1[ct1-1]
        else:
            if lista[ct] != lista1[ct]:
                return lista1[ct+1]