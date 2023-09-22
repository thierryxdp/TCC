def maiores(lista, n):
    '''Função que cria uma nova lista, mantendo a mesma em ordem crescente '''
    'int --> int'
    a = lista
    A = list(a) 
    n=int(n)
    
    list.append(A, n)
    list.sort(A)

    if n > max(lista):
        return []
    elif n < max(lista):
        N=list.index(A, n)
        list.sort(A)
        
        return A[N: ]