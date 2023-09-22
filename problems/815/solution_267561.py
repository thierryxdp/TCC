def insere([lista_numero, n]):
    '''função que insere um número n em uma lista lista_numero na sua posição ordenada dentro da mesma; list, int -> list'''
    
    lista_ordenada = list.append(lista_numero, n)
    lista_ordenada = list.sort(lista_numero)
    
    return lista_ordenada