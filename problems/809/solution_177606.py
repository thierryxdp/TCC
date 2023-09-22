def intercala(lista1, lista2):
    """Função que dadas duas listas L1 e L2 de tamanho 3,
    gera uma lista L3 que é formada intercalando os elementos
    de L1 e L2.
    list,list->list
    """
    L1 = lista1
    L2 = lista2
    return [*sum(zip(l2,l1),())]