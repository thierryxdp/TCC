def maiores(lista, n):
    '''Função que cria uma nova lista, mantendo a mesma em ordem crescente '''
    'int --> int'
    a = lista
    A = list(a) 
    n=int(n)
    
    list.append(A, n)
    list.sort(A)

    if (n) in list(A) or n < A[n] :
        return A[n:]
    else:
        []