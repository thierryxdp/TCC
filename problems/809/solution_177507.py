def intercala(lista1, lista2):
    """Intercala os elementos de duas listas com 3 elementos cada;
    list,list -> list"""
    lista3=lista1
    lista3[1]=lista2[0]
    lista3[3]=lista2[1]
    lista3[5]=lista2[2]
    return lista3