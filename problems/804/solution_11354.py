#Start your python function here
def filtra_pares(a,b,c,d):
    tuple=[a,b,c,d]
    if a%2==0:
        return tuple=(a)
    elif b%2==0:
        return tuple=(a,b)
    elif c%2==0:
        return tuple=(a,b,c)
    else:
        return tuple=(a,b,c,d)