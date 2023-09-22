def filtraMultiplos(x,n):
    b=[]
    i=0
    while i<len(x):
        if x[i]%n==0:
            b=b.append(x[i])
        i=i+1
        return b