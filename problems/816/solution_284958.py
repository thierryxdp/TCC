def maiores(listas, n):
    '''Funcao bla bla bla'''
    'list,int --> list'
    
    a=listas
    A=list(a)
    list.append(A, n)
    list.sort(A)
    
    if n in A:
        return A[1:]
        
    else:
        return []