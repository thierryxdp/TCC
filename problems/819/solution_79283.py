def filtraMultiplos(x,n):
    b=[]
    while x[0:]%n==0:
        b=b+x[0:]
    return b