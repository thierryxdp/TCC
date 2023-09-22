def filtraMultiplos(x,y):
    
    z = []
    indice = 0
    
    while x[indice] % y == 0:
        
          z.append(indice)
        indice += 1
        
    return z