def intercala(lista1, lista2):
    """Função que dadas duas listas L1 e L2 de tamanho 3,
    gera uma lista L3 que é formada intercalando os elementos
    de L1 e L2.
    list,list->list
    """
    L1 = lista1
    L2 = lista2
    L3 =[ ]
    for i in range(0,len(L1)):
        L3.append(L1[i]) L3.append(L2[i])
    return L3