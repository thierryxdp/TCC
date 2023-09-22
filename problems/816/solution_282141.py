def maiores(lista,n):
    """dada uma lista e um n retorna os numeros maiores que n"""
    concat = lista + [n]
    list.sort(concat)
    posicao_n = list.index(concat,n)
    lista_edit = concat[posicao_n:]
    lista2= list.remove(lista_edit,n)
    return lista_edit