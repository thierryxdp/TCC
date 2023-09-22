def maiores(listas, n):
    '''Funcao bla bla bla'''
    'list,int --> list'
    
    a=listas
    A=list(a)
    list.append(A, n)
    list.sort(A)
    
    if n in A:
        return A[0: ]
        
        
    elif n not in A[-1]:
        list.append(A, n)
        list.sort(A, n)
        return A[0:]
    else:
        []