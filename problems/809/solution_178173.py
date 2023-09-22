def intercala(lista1, lista2):
    """Dadas duas listas l1 e l2 de tamanho 3, deve retornar uma lista l3 que é formada intercalando os elementos de l1 e l2. list, list-->list."""
    return zip (lista1 + lista2)