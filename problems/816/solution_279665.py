# Dada uma lista e um número inteiro n,
# retorna todos da lista que são maiores que n
# list, int -> list
def maiores(lista, n):
    lista.append(n)
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]