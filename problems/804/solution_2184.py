#Start your python function here
def filtra_pares(tupla):
    tuple = ()
    t0 = int(tupla[0])
    t1 = int(tupla[1])
    t2 = int(tupla[2])
    t3 = int(tupla[3])
    if t0 % 2 == 0:
        tuple = tuple + (t0,)
    if t1 % 2 == 0:
        tuple = tuple + (t1,)
    if t2 % 2 == 0:
        tuple = tuple + (t2,)
    if t3 % 2 == 0:
        tuple = tuple + (t3,)
    return tuple