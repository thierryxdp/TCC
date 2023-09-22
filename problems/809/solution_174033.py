# Cria uma lista com os termos intercalados de duas outras listas
# lista1, lista2: listas
def intercala(lista1, lista2):
    """A partir de lista1 e lista2, de 3 elementos cada, cria-se uma terceira
    lista contendo os elementos de lista1 e lista2 intercalados (começando
    com o primeiro termo de lista1 e terminando com o terceiro termo de lista2
    lista1, lista2: lista
    return: lista"""
    return [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]