def intercala(l1, l2):
    """Dadas duas listas de tamanho 3 na estrada,
    retorna uma lista intercalando os elementos das
    listas de entrada
    list -> list"""
    lista3 = 6*[0]
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3