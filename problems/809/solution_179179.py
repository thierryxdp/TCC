def intercala(lista1, lista2):
    """Esta função intercala duas listas chamadas lista1 e lista2
    em ordem, gerando assim uma nova lista.
    list, list->list"""
    L1 = lista1
    L2 = lista2
    lista_resposta = list()
    lista_resposta += L1[0]+L2[0]+L1[1]+L2[1]+L1[2]+L2[2]