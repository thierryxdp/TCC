#Start your python function here
def filtra_pares(a):
    n1 = a[0]
    n2 = a[1]
    n3 = a[2]
    n4 = a[3]
    pares=( )
    if a[0] % 2 == 0 or a[1] % 2 == 0 or a[2] % 2 == 0 or a[3] % 2 == 0:
        pares = pares + (a[0],a[1],a[2],a[3],)
    return pares