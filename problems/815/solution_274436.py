def insere(lista_numero, n):
    ''' Função que insere um número 'n' em uma lista e ordena ela em ordem
    ascendente.     list=>list '''
    ordenada = lista_numero.insert(0,n)
    ordenada.sort(list)