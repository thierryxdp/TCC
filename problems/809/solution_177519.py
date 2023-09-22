def intercala(lista1, lista2):
    """Recebe duas listas que contém 3 elementos cada
e as agrupa em uma nova lista, depois retorna os
elementos originais de forma intercalada.
list, list -> list
"""
    lista3 = lista1 + lista2
    return lista3[:4:3]+lista3[1:5:3]+lista3[2::3]