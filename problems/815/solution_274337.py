def insere(lista_numero, n):
    ''' insre o numero n na posição correta em ordem na lista
    	list, int ---> list '''
    list.append(lista_numero,n)
    lista_numero = list.sort(lista_numero)
    return lista_numero