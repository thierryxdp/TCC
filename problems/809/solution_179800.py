def intercala(lista1, lista2):
    """Recebe duas listas L1 e L2 de tamanho 3 e gera uma lista L3 que é formada intercalando
    os elementos L1 e L2
    list, list -> list"""
    l3 = []
    l3 += lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]
    return l3