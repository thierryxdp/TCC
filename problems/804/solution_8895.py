#Start your python function here
def par(i):
    return i%2 == 0

def filtra_pares(tup):
    p = ()
    a,b,c,d = tup
    if par(a):
        p = p + (a,)
    if par(b):
        p = p + (b,)
    if par(c):
        p = p + (c,)
    if par(d):
        p = p + (d,)
    return p