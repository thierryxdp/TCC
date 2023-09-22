def insere (lista_numero, n):
    '''recebe uma lista e adiciona mais um numero a essa lista, retornando uma nova lista na ordem crescente'''
    '''list->list'''
    lista = lista_numero
    um = list.append(lista, n)
    list.sort(lista)
    return lista