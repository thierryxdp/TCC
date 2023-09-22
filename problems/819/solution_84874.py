def filtraMultiplos(x,y):
    
    x = []
    indice = 0
    
    while x[indice] % y == 0:
         
           x.append(indice)
           indice += 1
        
    return x