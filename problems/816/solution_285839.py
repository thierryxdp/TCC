def maiores(lista, n):
    """Esta funcao recebe uma lista, um numero n, e retorna outra lista que
    contem apenas os numeros maiores que n da lista original.
    Entrada: list [int, int, int, ..., int]
    Saida: list [int, int, int, ..., int]"""
    list.append(lista, n)
    list.sort(lista)
    return lista[list.index(lista, n)+1:]