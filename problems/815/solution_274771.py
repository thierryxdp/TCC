def insere (lista_numero,n):
    '''
       Dada uma lista e um número a função retorna uma nova 
       lista contendo a lista dada mais o número n dentro da
       nova lista de forma ordenada
       list, int -> list
    '''
    lista = list.append(lista_numero, n)
    lista = list.sort(lista)
    return lista