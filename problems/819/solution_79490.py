def filtraMultiplos(l,n):
    i=0
    a=[]
    while i<len(l):
        if l[i]%n==0:
            a = a + [l[i]]
        i=i+1
    return a