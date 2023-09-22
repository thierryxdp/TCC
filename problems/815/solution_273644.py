def insere(lista_numero, n):
    '''Função que insere um novo numero, mantendo a ordem crescente da lista'''
    'int --> int'
    x = lista_numero 
    
    n1 = int(n)
    n2 = list.index(x, n1)
    n3 = list.sort(n2)
    return n3