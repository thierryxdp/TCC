def filtra_pares (t):
    '''essa função retorna uma tupla apenas com os numeros inteiros pares da tupla original. 
    tupla (int) -> tupla (int)'''
    
        t= (())
        if t[0]%2==0:
            t = t + (t[0],)
        else:
            t=t
        if t[1]%2==0:
            t= t + (t[1],)
        else:
            t=t
        if t[2]%2==0:
            t = t + (t[2],)
        else:
            t=t
        if t[3] %2==0:
            t = t+ (t[3],)
        else:
            t= t
            
        return t