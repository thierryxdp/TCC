def maiores(lista,n):
    """dada uma lista e um n retorna os numeros maiores que n"""
    list.sort(lista)
    posicaon = list.index(lista,n)
    listaedit = lista[n:]
    return listaedit