def insere(lista_numero, n):
    '''Esta funcao inclui um numero numa lista na ordem certa.'''
    '''list --> list'''
    lista_ordenada = list.append(lista_numero, n)
    list.sort(lista_ordenada)
    return lista_ordenada