def intercala(lista1, lista2):
    """Função que dadas duas listas L1 e L2 de tamanho 3,
    gera uma lista L3 que é formada intercalando os elementos
    de L1 e L2.
    list,list->list
    """
    L3 = str(lista1) + str(lista2)
    return L3[1] + L3[4] + L3[2] + L3[5] + L3[3] + L3[6]