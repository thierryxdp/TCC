def filtraMultiplos(m,n):
    pos = 0
    contador = []
    
    while n > m[0]:
        if m[pos] % n == 0:
            list.append(contador,m)
        else:
            list.append([])
            
        pos = pos +1 
            
    return contador