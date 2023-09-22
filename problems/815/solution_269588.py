def insere (lista_numero, n):
    '''Insere um número n la lista  e a mesma continua ordenada
    tupla-> lista'''
    lista = list.append(lista_numero, n)
    lista_ordenada = list.sort(lista)
    return lista_ordenada