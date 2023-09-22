def filtra_pares (a):
    """esta e a funçao filtra_pares que recebe uma tupla com 4 elementos inteiros e retorna somente os valores pares"""
    y = ()
    
    if ( a[0]%2 ) == 0:
        y = y + (a[0],)
        
    if ( a[1]%2 ) == 0:
        y = y + (a[1],)
        
    if ( a[2]%2 ) == 0:
        y = y + (a[2],)
        
    if ( a[3]%2 ) == 0:
        y = y + (a[3],)
        
        return y