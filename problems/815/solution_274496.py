def insere(lista_numero, n):
    '''inclue um número n na lista crescente dada (lista_numero), de forma que a lista continue ordenada
    list, int -> list'''
    lista_numero.append(n)
    lista_nova = lista_numero.sort()
    return lista_nova