#Start your python function here
def par(y):
    if y%2 == 0:
        return y

def filtra_pares(x):
    t = ()
    n1 = par(x[0])
    n2 = par(x[1])
    n3 = par(x[2])
    n4 = par(x[3])
    t = (n1, n2, n3, n4)
    return t