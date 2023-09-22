def intercala(lista1, lista2):
    """a partir da lista1 e lista2 de 3 elementos cada
    retorna uma lista que intercala seus elementos"""
    lista=str(lista1[0])+str(lista2[0])+str(lista1[1])+str(lista2[1])+str(lista1[2])+str(lista2[2])
    return list(lista)