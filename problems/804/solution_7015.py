#Start your python function here
def par(y):
    if y%2 == 0:
        return str(y)

def filtra_pares(x):
    t = ()
    n1 = par(x[0])
    if n1:
        t += (n1,)
    n2 = par(x[1])
    if n2:
        t += (n2,)
    n3 = par(x[2])
    if n3:
        t += (n3,)
    n4 = par(x[3])
    if n4:
        t += (n4,)
    return t