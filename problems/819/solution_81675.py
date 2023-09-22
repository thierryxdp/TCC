"""Recebe uma lista de números e retorna os elementos que forem dividos por n:
int->int"""
def filtraMultiplos(lista,n):
    lista1 = []
    i = 0
    while i < len(lista):
     	if lista[i]%n == 0:
            list.append(lista1, lista[i])
    return lista1