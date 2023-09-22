def insere(lista_numero, n):
    '''a funcao insere um numero n na lista de forma que continue ordenada
list[str], str'''
    n=[n]
    lista_nova=lista_numero+n
    list.sort(lista_nova)
    return lista_nova