def insere(lista_numeros,n):
    '''Função que dada uma lista ordenada e um numero inteiro
    n como entrada retorne a lista incluindo o n de maneira
    ordenada. list, int --> list.'''
    lista_numeros.append(n)
    list.sort(lista_numeros)
    return lista_numeros