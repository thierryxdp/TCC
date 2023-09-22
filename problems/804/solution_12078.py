def filtra_pares(a):
    '''retorna os elementos pares de uma tupla de quatro elementos inteiros'''
    '''int, int, int, int -> int, ...'''
    b = ()
    
    if round((a[0])%2) == 0:
        b = b+(a[0],)
    
    if round((a[1])%2) == 0:
        b = b+(a[1],)
    
    if round((a[2])%2) == 0:
        b = b+(a[2],)
    
    if round((a[3])%2) == 0:
        b = b+(a[3],)
        
    else:
        ()
    
        return b