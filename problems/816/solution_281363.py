def maiores(lista_numero,n):
    '''Recebe uma lista de números e retorna uma nova lista somente com os valores maiores que o valor de entrada n; list->list'''
    list.sort(lista_numero)
    return lista_numero[n+1:]