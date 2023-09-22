def filtraMultiplos (ls, n):
    r=[]
    c=0
    while c<=len(ls):
        if ls[c]%n==0:
            r.append(ls[c])
        c=c+1
    return r