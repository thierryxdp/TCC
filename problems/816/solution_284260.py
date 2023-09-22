def maiores(lista,n):
    """Dada uma lista e um numero, irá me retornar outra lista mas nela contendo o numero inteiro passado
com os numeros maiores em ordem crescente list.int->list"""
    list = lista
    list.append(n)
    list.sort()
    list = list[list.index(n)+1):]
    return list