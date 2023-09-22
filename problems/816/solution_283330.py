def maiores(lista, n):
    """Dada uma lista de numeros inteiros e um numero inteiro, retorna uma lista que contem os numeros da lista original maiores que n, em ordem crescente"""
    x = lista
    list.insert(x, 0, n)
    a = sorted(x)
    b = list.index(a, n)
    del a[:b + 1:1]
    return a