#Start your python function here
def filtra_pares(a):
    pares=()
    if a[0] % 2 == 0 and a[1] % 2 == 0:
        pares.append(a[0],a[1],a[2],a[3])
    return pares