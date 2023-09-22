def intercala(lista1, lista2):
    """Funcao que gera uma lista formada pelos elementos das outras listas"""
    lista1 = [::2]
    lista2 = [1::2]
    return lista1 + lista2