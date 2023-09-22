def par(x):
    if x%2 == 0:
        return (x,)
    else:
        return tuple()

def filtra_pares (n1,n2,n3,n4):
   	n1=par(n1)
    n2=par(n2)
    n3=par(n3)
    n4=par(n4)
    tuplapar= n1+n2+n3+n4
    return tuplapar