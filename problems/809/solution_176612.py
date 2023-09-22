def intercala(lista1, lista2):
    """a função recebe duas listas e devolve uma lista nova, todos os elementos dessa lista nova são provenientes da intercal
    ação dos elementos das listas 1 e 2; list, list -> list"""
	lista12 = lista1 + lista2
    lista12[0::2] = lista1
    lista12[1::2] = lista2
    return lista12