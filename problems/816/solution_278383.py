'''Retorna os elementos de uma lista que são maiores do que o número n informado
list, int -> list'''
def maiores(lista, n):
    lista += [n]
    lista.sort()
    return lista[lista.index(n)+1:]