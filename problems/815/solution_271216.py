def insere(lista_numero, n):
    '''Função que recebe uma lista ordenada de números inteiros
    e um número inteiro separado, e o coloca dentro dessa lista
    a mantendo ordenada.
    [list], int -> [list]'''
    lista_numero = lista_numero + [n]
    list.sort(lista_numero)
    
    return lista_numero