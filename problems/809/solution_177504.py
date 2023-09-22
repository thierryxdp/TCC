def intercala(lista1, lista2):
    """Intercala os elementos de duas listas com 3 elementos cada;
    list,list -> list"""
    lista3=lista1
    lista3[2]=lista2[1]
    lista3[4]=lista2[2]
    lista3[6]=lista2[3]
    return lista3