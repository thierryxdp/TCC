import random
def faltante(lista):
    """esta função recebe uma lista de números e retorna os números faltantes desta lista
    list-> int"""
    lista.sort()
    indice=0
    a=len(lista)-1
    N=lista[a]
    lista1=random.randint(1,N)
    while indice<len(lista):
        if [lista[indice]] in random.randint(1,N):
            lista2=[lista[indice]]
        if len(lista)==1 and lista[indice]!=1:
            return random.randint(1,lista[indice])
        return lista[indice]