def intercala(lista1,lista2):
    """Fatia as listas e as organiza de forma a intercalar l1 e l2
    list + list -> list"""
    lista3 = lista1 + lista2
    lista3[::2] = lista1
    lista3[1::2] = lista2
    return lista3