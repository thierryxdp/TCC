def filtraMultiplos(m,n):
    pos = 0
    resultado = []
    while n < len(m):
        
        if m[pos] % n == 0:
            list.append(resultado,m)
        else:
            list.append(resultado,[])
        pos = pos + 1
       
    return resultado