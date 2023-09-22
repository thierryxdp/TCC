def filtraMultiplos(m,n):
    pos = 0
    resultado = 0
    while pos < len(m):
        
        if m[pos] % n == 0:
            list.append(resultado,m)
        pos = pos + 1
    return resultado