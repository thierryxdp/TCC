def fm(x,n):
    if x%n==0:
       return True
def filtraMultiplos(x,n):
    r=[]
    for e in x:
        if filtraMultiplos(x,n):
            r.append(x)
    return r