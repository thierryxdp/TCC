def intercala(lista1, lista2):
    """Dados a lista1 e a lista2, a função retorna uma lista3 que intercala os elementos da lista1 e lista2
    list,list->list"""
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]+[lista1[3]]+[lista2[3]]