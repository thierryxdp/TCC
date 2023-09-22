def maiores(lista, n):
    """Recebe uma lista de números inteiros e um número inteiro n,
retorna uma lista que contém todos os números da lista inserida
que sejam maiores do que n de forma crescente através de ordenação
e indexação.
list, int -> list
"""
    if n in lista:    
        lista_completa = lista[:]
    else:
        lista_completa = lista[:] + [n]
    list.sort(lista_completa)
    indice = list.index(lista_completa, n)
    return lista_completa[indice+1:]