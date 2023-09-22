def intercala(L1, L2):
    """Dados a lista1 e a lista2, a função retorna uma lista3 que intercala os elementos da lista1 e lista2
    list,list->list"""
    return [L1[0]]+[L2[0]]+[L1[1]]+[L2[1]]+[L1[2]]+[L2[2]]