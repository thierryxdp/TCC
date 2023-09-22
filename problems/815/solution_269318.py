def insere(lista_numero, n):
    '''Função que dada uma lista ordenada de números inteiros e um número
    inteiro n, inclua n no local correto, mas a lista deve continuar
    ordenada.'''
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero