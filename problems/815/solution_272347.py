def insere(lista_numero, n):
    '''Funçao que dado uma lista e um número, vai retornar uma outra lista com esse número inserido e na ordem crescente.
    list, int->list'''
    l=lista_numero[:]
    list.append(l, n)
    list.sort(l)
    return l