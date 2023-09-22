def maiores(lista, n):
    """dado uma lista de entrada e um numero inteiro,calcula e retorna uma lista original maiores que n em ordem crescente
    lista,int-->lista """
    x = lista
    list.insert(x, 0, n)
    a = sorted(x)
    b = list.index(a, n)
    del a[:b + 1:1]
    return a