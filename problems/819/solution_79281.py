def filtraMultiplos(x,n):
    b=[]
    i=[0,1,2,3,4,5,6,7,8,9,10]
    while x[i]%n==0:
        b=b+x[i]
    return b