#Start your python function here
def filtra_pares(a,b,c,d):
    par = ()
    if a%2==0:
        par = par + (a)
    if b%2==0:
        par = par + (b)
    if c%2==0:
        par = par + (c)
    if d%2==0:
        par = par + (d)
    return par