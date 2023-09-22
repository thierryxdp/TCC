def filtraMultiplos(x,y):
    
    z = []
    indice = 0
    
    while x[indice] % y == 0:
        
           indice += 1
           z.append(indice)
        
    return z