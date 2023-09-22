def insere(lista_numero,n):
    """Dada uma lista e um número, insere-se o número na lista e retorna este ordenado. list,int -> list"""
    list.extend(lista_numero,[n])
    list.sort(lista_numero)
    return lista_numero