def maiores(lista, n):
    '''Função que cria uma nova lista, mantendo a mesma em ordem crescente '''
    'int --> int'
    a = lista
    A = list(a) 
    
    list.append(A, n)
    list.sort(A)

    if n in A :
        return A[n: ]
    else:
        []