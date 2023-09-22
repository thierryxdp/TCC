def maiores(lista, n):
    """Dada uma lista de números inteiros e um numero inteiro n, retorna uma lista contendo os numeros da lista original maiores que n, em ordem crescente
    list, int -> list"""
    x = lista
    list.insert(x, 0, n)
    a = sorted(x)
    b = list.index(a, n)
    del a[:b + 1:1]
    return a