def filtra_pares (a):
    """esta e a funçao filtra_pares que recebe uma tupla com 4 elementos inteiros e retorna somente os valores pares"""
    b = ()
    
    if ( a[0]%2 ) == 0:
        b = b + (a[0],)
        
    if ( a[1]%2 ) == 0:
        b = b + (a[1],)
        
    if ( a[2]%2 ) == 0:
        b = b + (a[2],)
        
    if ( a[3]%2 ) == 0:
        b = b + (a[3],)
        
    return b