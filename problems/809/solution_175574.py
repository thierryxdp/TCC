def intercala(lista1, lista2):
    """Funcao que dada duas listas de tamanho 3, gera uma outra lista que eh formada
intercalando os elementos das duas listas; list, list -> list"""
    L1 = lista1
    L2 = lista2
    L3 = L1[0], L2[0], L1[1], L2[1], L1[2], L2[2]
    return list(L3)