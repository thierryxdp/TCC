def maiores(L,n):
"""Função que retorna uma nova lista com os numeros maiores
    que da lista dada  em ordem crescente.
    list, int->list"""
    lista = L[list.index(L,n):]
    list.sort(L)
    return lista