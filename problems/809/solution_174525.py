def intercala(lista1, lista2):
    """Retorna uma lista intercalada com os elementos de duas listas de entrada"""
    #list -> list
    A = lista1[0]
    B = lista2[0]
    C = lista1[1]
    D = lista2[1]
    E = lista1[2]
    F = lista2[2]
    Lista = A, B, C, D, E, F
    return list(Lista)