def intercala(lista1, lista2):
    """Função que dadas duas listas L1 e L2 de tamanho 3, gera 
    uma lista L3 que é formada intercalando os ellementos de L1 e L2;
    list->list"""
    lista3 = lista1 + lista2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3