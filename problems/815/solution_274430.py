def insere(lista_numero, n):
    ''' Função que insere um número 'n' em uma lista e ordena ela em ordem
    ascendente.     list=>list '''
    conver = str(n)
    lista_numero.insert(0,conver)
    list.sort(lista_numero)