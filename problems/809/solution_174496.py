#Para gerar uma lista 3 intercalada juntei as 2 listas e juntas elas me retornam uma tercera
#
def intercala(lista1, lista2):
    """A função intercala os elementos da lista1 com a 2:
    list -> list"""
    lista3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    return lista3