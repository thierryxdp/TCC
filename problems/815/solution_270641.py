def insere(lista_numeros,n):
    '''Função que dada uma lista ordenada e um numero inteiro
    como entrada, retorne a lista com o numero ordenado.
    list, int --> list.'''
    lista_numeros= lista_numeros.append(n)
    list.sort(lista_numeros +[n])
    return lista_numeros