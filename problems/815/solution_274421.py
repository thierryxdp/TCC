def insere(lista_numero, n):
    '''
    Funcao que recebe uma lista de numeros ordenados e um numero inteiro (n). A funcao retorna
    uma nova lista ordenada incluindo o novo numero (n).
    list, int -> list
    '''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero