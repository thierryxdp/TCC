def intercala(l1, l2):
    """Dadas duas listas de tamanho 3 na estrada,
    retorna uma lista intercalando os elementos das
    listas de entrada
    list -> list"""
    l3 = 6*[0]
    l3[::2] = l1
    l3[1::2] = l2
    return l3