"""Retorna uma lista que é a combinaão da lista1 e lista2.
list, list -> list"""
def intercala(lista1, lista2):
    return list(volta(lista1, lista2))
def volta(lista1, lista2):
    return lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]