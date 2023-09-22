def filtraMultiplos(x,n):
    b=[]
    i=int
    while x[i]%n==0:
        b=b+x[i]
    return b