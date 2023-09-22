def interc(lista1, lista2):
    """Pede duas listas de 3 elementos cada
    e retorna uma lista com 6 elementos, formada
    intercalando-se os elementos das duas primeiras listas.
    list, list->list"""
    lista3=[]
    lista3=lista3+[lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return lista3