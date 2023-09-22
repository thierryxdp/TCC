def intercala(lista1, lista2):
    """Funçao que dada duas listas, Lista L1 e L2, retorna uma lista L3 que intercala os valores de L1 e L2.
    list,list->list"""
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]