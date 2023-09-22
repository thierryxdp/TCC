def intercala(lista1, lista2):
    """Função que retorna uma lista L3, intercalando os elementos
    da lista1 e lista2
    lista1=list,lista2=list->list"""
    L1 = [list(lista1)]
    L2 = [list(lista2)]
    L3 = [list(lista1) + list(lista2)]
    return L3