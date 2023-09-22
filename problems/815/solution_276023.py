def insere(lista_numero, n):
    '''funcao recebe uma lista de numeros e um numero, coloca o numero a lista, ordena e volta lista. list, int-->list'''
    lista_numero.insert(0, n)
    list.sort(lista_numero)
    return lista_numero