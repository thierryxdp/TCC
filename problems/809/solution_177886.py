def intercala(lista1: list, lista2: list)-> list:
    """Retorna uma lista L3 formada pelos elementos da lista L1 e da lista L2
    intercalados"""
    return lista1[0] + lista2[0] + lista1[1] + lista2[1] + lista1[2] + lista2[2]