def filtraMultiplos(m,n):
    pos = 0
    contador = []
    
    while m[pos] % n == 0:
           contador.append(m)
            
        else: 
            
             contador.append([])
        pos = pos +1
    return contador