def insere(lista_numero, n):
    '''Função que insere um novo numero, mantendo a ordem crescente da lista'''
    'int --> int'

    n = int(n)
    n1 = list.index(lista_numero,n)
    n2 = list.sort(n1)
    return list(n)