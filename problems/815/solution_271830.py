def insere(lista_numero, n):
    """ dada uma lista em ordem crescente, inclue n na posição correta)
    list, int -> list"""
    lista = list.append(lista_numero, n)
    list.sort (lista)
    return lista