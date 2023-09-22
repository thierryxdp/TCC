def maiores(lista,n):
    """dada uma lista e um n retorna os numeros maiores que n"""
    concat = lista + [n]
    list.sort(lista)
    posicaon = list.index(lista,n)
    listaedit = concat[n:]
    list.del(concat,n)
    return concat