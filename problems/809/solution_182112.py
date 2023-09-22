def intercala(lista1,lista2):
    """a partir do fatiamento a funcao intercala as listas de entrada
    list + list -> list"""
    l3 = lista1 + lista2
    l3[::2] = lista1
    l3[1::2] = lista2
    return l3