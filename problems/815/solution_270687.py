def ordenada (lista):
    ''' funçao ordenada que dada uma lista, retorne uma tupla'''
    '''list->tuple'''
    crescente = lista[:]
    crescente.sort()
    decrescente = lista[:]
    decrescente.sort(reverse=True)
    if lista == crescente:
        return (True, "crescente")
    elif lista == decrescente:
        return (True, "decrescente")
    else:
        return (False, "desordenada")