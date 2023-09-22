def filtraMultiplos(m,n):
    pos = 0
    contador = []
    
    while n > m[0]:
        if m[pos] % n == 0:
            contador.append(m)
        else:
            contador.append(m)
            
        pos = pos +1 
            
    return contador