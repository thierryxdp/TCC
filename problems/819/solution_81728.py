def filtraMultiplos(lista,n):
    """função que retorna os multiplos de um numero dado,
    dada uma lista de numero
    list,int=>list"""
    i = 0
    listaF = []

    while i<len(lista):
        if lista[i]%n==0:
            listaF+=[lista[i]]
        i+=1
    return listaF