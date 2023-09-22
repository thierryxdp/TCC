#Start your python function here filtra_pares([4,4,4,4]) ==(4, 4, 4, 4)'''
def filtra_pares(x):
    p = ()
    if par(x[0]):
        p = p + (x[0],)
    if par(x[1]):
        p = p + (x[1],)
    if par(x[2]):
        p = p + (x[2],)
    if par(x[3]):
        p = p + (x[3],)
    return p