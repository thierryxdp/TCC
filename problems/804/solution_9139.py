#Start your python function here
def filtra_pares(a,b,c,d):
    par = ()
    if (a%2==0):
        par = par + str(a)
    if (b%2==0):
        par = par + str(b)
    if (c%2==0):
        par = par + str(c)
    if (d%2==0):
        par = par + str(d)
    return par