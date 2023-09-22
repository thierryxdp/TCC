def insere (lista_numero, n):
    '''Insere um número n la lista  e a mesma continua ordenada
    tupla-> lista'''
    lista = lista_numero.append(n)
    lista_ordenada = lista.sort()
    return lista