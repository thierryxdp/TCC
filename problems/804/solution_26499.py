def filtra_pares(ls):
    ln = ()
    
    if ls[0] % 2 == 0:
        ln.extend(ls[0])
        
    if ls[1] % 2 == 0:
        ln.extend([ls[1]])
        
    if ls[2] % 2 == 0:
        ln.extend([ls[2]])
        
    if ls[3] % 2 == 0:
        ln.extend([ls[3]])
    
    return ln