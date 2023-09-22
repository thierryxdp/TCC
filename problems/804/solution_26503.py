def filtra_pares(l):
    ls = list(l)
    ln = ()
    
    if ls[0] % 2 == 0:
        ln.append(int(ls(0)))
        
    if ls[1] % 2 == 0:
        ln.extend([ls[1]])
        
    if ls[2] % 2 == 0:
        ln.extend([ls[2]])
        
    if ls[3] % 2 == 0:
        ln.extend([ls[3]])
    
    return ln