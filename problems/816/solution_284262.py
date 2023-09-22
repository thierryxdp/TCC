def maiores(lista,n):
    """dada uma lista e um numero, a funçao me retorna outra lista contendo o numero inteiro passado
com os numeros maiores em ordem crescente; list,int->list"""
    list = lista
    list.append(n)
    list.sort()
    list = list[(list.index(n)+1):]
    return lst