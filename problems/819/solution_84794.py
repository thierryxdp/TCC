def filtraMultiplos(ls,n):
    r = []
    i = 0
    while i < len(ls):
        if ls[i]%n==0: 
            return r.append(ls[i])