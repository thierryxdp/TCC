def filtraMultiplos(x,n):
    b=0
    i=0
    while x[i] in x:
        x[i]%n==0
        b=b+x[i]
        i=i+1
    return [b]