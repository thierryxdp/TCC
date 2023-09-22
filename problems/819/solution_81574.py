def filtraMultiplos(n,p):
    m = 0
    mult = []
    while m <len(n):
        if n[m]%p == 0:
            mult += n[m],
            m = m + 1
        else:
            m = m + 1
    
    return mult