def filtra_pares(a,b,c,d):
    ''' retorna uma nova tupla contendo os numeros pares da tupla informada como parametro'''
    ''' (int, int, int, int) -> (int,...)'''
    t = (a,b,c,d)
    t2 = ()
    
    if t[0]% 2 == 0:
        t2 = t2 + (t[0])
    
    if t[1]% 2 == 0:
        t2 = t2 + (t[1])
        
    if t[2]% 2 == 0:
        t2 = t2 + (t[2])
        
    if t[3]% 2 == 0:
        t2 = t2 + (t[3])
        
    return t2