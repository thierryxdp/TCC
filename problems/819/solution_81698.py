"""Recebe uma lista de números e retorna os elementos que forem dividos por n:
list, int->int"""
def filtraMultiplos(lista,n):
    listaM = []
    i=0
    while i<len(lista):
     	if lista[i]% n == 0:
            list;append(listaM, lista[i])
        i = i+1
    return listaM