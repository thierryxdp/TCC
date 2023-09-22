# Retorna uma lista que intercala os elementos das duas listas dadas
def intercala(lista1, lista2):
    """
    Retorna uma lista que intercala os elementos das duas listas dadas
    list, list -> list
    """
    return [lista1[0]+lista2[0]+lista1[1],lista2[1]+lista1[2]+lista2[2]]