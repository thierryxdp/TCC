def intercala(lista1, lista2):
    """Função que retorna uma lista que intercala duas listas dadas
    list, list -> list"""
    c=[*sum(zip(lista2,lista1),())]
    return c