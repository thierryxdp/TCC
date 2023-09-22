def filtraMultiplos (x, n):
    r=[]
    c=0
    while c<=len(x):
        if x[c]%n==0:
            r.append(x[c])
        c=c+1
    return r