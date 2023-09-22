def maiores(lista, n):
    """ dado uma lista de números inteiros e o inteiro n, retorna outra lista com todos os números maiores que n ordenados em ordem crescente
    list, int -> list"""
    list.append (lista,n)
    list.sort(lista)
    indice = list.index (lista, n)
    lista = lista[indice+1:]
    return lista