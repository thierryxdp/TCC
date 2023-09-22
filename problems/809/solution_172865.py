def intercala(lista1, lista2):
    """essa função usa as listas de entrada para criar uma nova lista, intercalando os elementos das outras duas"""
    return [*sum(zip(lista1, lista2),())]