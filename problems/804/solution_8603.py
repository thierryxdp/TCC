#Start your python function here
def filtra_pares(x):
    s = ()
 	x = list(x)
    if x[0:1]%2 == 0:
        s = x[0:1]
    if x[1:2]%2 == 0:
        s = x[1:2]
    if x[2:3]%2 == 0:
        s = x[2:3]
    if x[3:4]%2 == 0:
        s = x[3:4]
    return s