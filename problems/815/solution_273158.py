def insere(lista_numero, n):
    """ dada uma lista e um numero n, retorna uma lista nova
    que inclui o numero n de modo com que a lista fque ordenada
    list, int -> list"""
    nova = lista_numero.append(n)
    return list.sort(nova)