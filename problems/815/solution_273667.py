def insere(lista_numero, n):
    '''Função que insere um novo numero, mantendo a ordem crescente da lista'''
    'int --> int'
    a = lista_numero
    A = list(a)
    list.append(A, n)
    list.sort(A)
           
    return A