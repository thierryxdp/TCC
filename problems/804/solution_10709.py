def filtra_pares (a):
    '''filtragem''' 
    b = ()
    
    if a[0]% 2 != 0:
    b = b + (a[2],)
        
    if a[1]% 2 != 0:
    b = b + (a[4],)
        
    if a[2]% 2 != 0:
    b = b + (a[6],)
        
    if a[3]% 2 != 0:
    b = b + (a[8],)
        
    return b