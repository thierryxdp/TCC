def intercala(lista1, lista2):
    """gera uma lista, formada intercalando os elementos da lista1 e lista2.
    list->list"""
    lista1.insert(lista2[0],1)
    lista1.insert(lista2[1],3)
    lista1.insert(lista2[2],5)
    return c