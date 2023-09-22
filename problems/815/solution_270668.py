def insere(lista,n):
    '''insere elemento n na lista e retorna a lista
    ordenada
    list,int->list'''
    l = lista[:]
    l.append(n)
    l.sort()
    return l