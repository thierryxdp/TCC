def maiores(lista,n):
    """dada uma lista e um n retorna os numeros maiores que n"""
    concat = lista + [n]
    list.sort(concat)
    posicaon = list.index(concat,n)
    listaedit = concat[n:]
    list.remove(concat,n)
    return concat