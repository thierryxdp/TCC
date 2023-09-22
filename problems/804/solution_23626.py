def filtra_pares(tupla):
    t = ()
    if tupla[0]%2==0:
        t+=(tupla[0],)
        
    if tupla[1]%2==0:
        t+=(tupla[1],)
    
    if tupla[2]%2==0:
        t+=(tupla[2],)
        
    if tupla[3]%2==0:
        t+=(tupla[3],)
     
    return t