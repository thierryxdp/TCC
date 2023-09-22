def intercala(lista1, lista2):
    """gera uma lista, formada intercalando os elementos da lista1 e lista2.
    list->list"""
    lista1.insert(1,lista2[0])
    lista1.insert(3,lista2[1])
    lista1.insert(5,lista2[2])
    return lista1