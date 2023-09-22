def insere(lista_numero,n):
    ''' Essa função recebe uma lista e um numero n e adiciona n na lista e ordena a mesma.'''
    '''Entrada = lista ; Saída = lista'''
    lista_nova = lista_numero.append(n)
    lista2 = lista_nova.sort()
    return lista2