def filtraMultiplos(ls, n):
    r=[]
    for i in ls:
        if i%n==0:
            
            r.append(i)
    return r