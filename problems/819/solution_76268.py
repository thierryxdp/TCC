def filtraMultiplos(m,n):
    pos = 0
    resultado = []
    while pos < len(m):
        
        x =  m[pos] % 2 == 0
        
        if m[pos] % 2 == 0:
            list.append(resultado,x)
        else:
            list.append(resultado,[])
        pos = pos + 1
       
    return resultado