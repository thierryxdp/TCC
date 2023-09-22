def filtraMultiplos(x,n):
    b=0
    i=0
    while i<len(x):
        if x[i]%n==0:
            b=b+x[i]
        i=i+1
        c=[b]
    return [b]