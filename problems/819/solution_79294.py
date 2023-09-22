def filtraMultiplos(x,n):
    b=[]
    i=0
    while x[i]%n==0:
        b=b+[x[i]]
    return b