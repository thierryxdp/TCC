def filtra_pares (t):
    '''essa função retorna uma tupla apenas com os numeros inteiros pares da tupla original. 
    tupla (int) -> tupla (int)'''
    x=()
    
        if t[0]%2==0:
            x = x + (t[0],) 
        else:
            x=x
            
        if t[1]%2==0:
            x= x + (t[1],)
        else:
            x=x
            
        if t[2]%2==0:
            x = x + (t[2],)
        else:
            x=x
            
        if t[3] %2==0:
            t = t+ (t[3],)
        else:
            x=x
            
        return x