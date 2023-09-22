import random
def faltante(lista):
    """esta função recebe uma lista de números e retorna os números faltantes desta lista
    list-> int"""
    lista=lista.sort()
    indice=0
    a=(len(lista)-1)
    N=lista[a]
    lista1=randint(1,N)
    while indice<len(lista):
        if lista[indice] in lista1(1,N):
            lista2=[lista[indice]]
        return lista[indice]