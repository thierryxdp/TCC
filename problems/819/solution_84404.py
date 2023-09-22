def filtraMultiplos (ls, n):
    r=[]
    c=0
    while c<=len(ls):
        ls[c]%n==0
        c=c+1
        r=r+ ls[c]
    return r