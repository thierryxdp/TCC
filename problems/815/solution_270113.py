def insere(lista_numero,n):
    '''Funcao que insere o numero n na lista e retorna ela ordenada
    ;list->list'''
    a=lista_numero
    a.append(n)
    a.sort()
    return a