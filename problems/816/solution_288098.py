def maiores(lista, n):
    """funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista
    contendo todos os numeros da lista original maiores que n, ordenados em ordem crescente;
    list, int -> list"""
    list.insert(lista, 1, n)
    list.sort(lista)
    if max(lista) == n:
        return []
    if list.index(lista, n) == 0:
        list.remove(lista, n)
        return lista
    if list.index(lista, n) > 0:
        x = list.index(lista, n)
        del lista[0:x+1]
        return lista