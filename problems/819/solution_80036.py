def filtraMultiplos(l,n):
    
    i = 0
    ln = []
    while i<len(l):
        if l[i]%n==0:
            ln += l[i]
        i += 1
    return ln