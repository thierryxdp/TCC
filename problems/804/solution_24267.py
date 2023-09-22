def filtra_pares (a):
    '''essa função retorna uma tupla apenas com os numeros inteiros pares da tupla original. 
    tupla (int) -> tupla (int)'''
    x= ()
    
    if a[0]%2 == 0:
        x=x + (a[0], )
    else:
        x=x
        
    if a[1] %2 == 0:
        x=x + (a[1], )
    else:
        x=x
    
    if a[2] %2 ==0:
        x=x + (a[2], )
    else:
        x=x
        
    if a[3] %2 == 0:
        x=x + (a[3], )
    else:
        x=x
        
    return x