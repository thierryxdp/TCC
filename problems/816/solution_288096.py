def maiores(lista, n):
    """funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista
    contendo todos os numeros da lista original maiores que n, ordenados em ordem crescente;
    list, int -> list"""
    list.insert(lista, 1, n)
    list.sort(lista)
    if n-1 > 0:
        list.del(lista,[list.index(lista, n-1)])
    if n-2 > 0:
        list.del(lista,[list.index(lista, n-2)])
    if n-3 > 0:
        list.del(lista,[list.index(lista, n-3)])
    elif n-1 or n-2 or n-3 == 0:
        list.sort(lista)
        return lista
    return lista