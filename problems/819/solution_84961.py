def filtraMultiplos(x,n):
    if x%n==0:
        return True
def fm(x,n):
    r=[]
    for x in ls:
        if filtraMultiplos(x,n):
            r.append(x)
    return r