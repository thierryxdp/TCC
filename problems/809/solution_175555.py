def intercala(lista1, lista2):
    """Função que retorna uma lista L3, intercalando os elementos
    da lista1 e lista2
    lista1=list,lista2=list->list"""
    L1 = list(lista1)
    L2 = list(lista2)
    L3 = list(lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2],lista1[3],lista2[3])
    return L3