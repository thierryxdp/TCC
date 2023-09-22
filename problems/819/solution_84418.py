def filtraMultiplos(ls,n):
    k=[]
    for i in ls:
        if i%n==0:
            k+=[i]
    return k