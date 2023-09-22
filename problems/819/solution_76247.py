def filtraMultiplos(m,n):
    pos = 0
    contador = []
    
    while n > m[0]:
        if (m[pos] % n) == 0:
            contador.append('impar')
        else:
            contador.append('impar')
            
        pos = pos +1 
            
    return contador