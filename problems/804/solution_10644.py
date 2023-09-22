def filtra_pares (a):
    '''recebe uma tupla, calcula e retorna uma nova tupla contendo apenas os elementos pares da original'''
    '''tuple->tuple (pares)'''
    
    b = ()
    
    if a[0]% 2 == 0:
        b = b + (a[0],)
       
    if a[1]% 2 == 0:
        b = b + (a[1],)
        
    if a[2]% 2 == 0:
        b = b + (a[2],)
        
    if a[3]% 2 == 0:
        b + b + (a[3],)
    return b