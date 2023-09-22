def intercala(lista1, lista2):
    """Função que dadas duas listas L1 e L2 de tamanho 3,
    gera uma lista L3 que é formada intercalando os elementos
    de L1 e L2.
    list,list->list
    """
    vazio = ()
    con = vazio + str(lista1) + str(lista2)
    L3 = con[1] + con[4] + con[2] + con[5] + con[3] + con[6]
    return L3