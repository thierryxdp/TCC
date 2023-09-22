def filtraMultiplos(m,n):
    pos = 0
    contador = []
    
    while pos > m[0]:
        if m[pos] % n == 0:
            list.append(contador)
        else:
            list.append([])
            
        pos = pos +1 
            
    return contador