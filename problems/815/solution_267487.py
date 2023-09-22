def insere(lista_numero, n):
    '''dada uma lista ordenada e um numero n, retorna a mesma lista com n de modo que ela continue em ordem
    list, int -> list'''
    index = 0
    for i in lista_numero:
        if n > i:
            index += 1
    list.insert(lista_numero, index, n)
    return lista_numero