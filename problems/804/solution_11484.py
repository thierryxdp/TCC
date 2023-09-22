def filtra_pares(tup):
    
    par = ( )
    
    if tup[0] % 2 == 0:
        par += (tup[0],)
    
    if tup[1] % 2 == 0:
        par += (tup[1],)
        
    if tup[2] % 2 == 0:
        par += (tup[2],)
        
    if tup[3] % 2 == 0:
        par += (tup[3],)
        
        return par