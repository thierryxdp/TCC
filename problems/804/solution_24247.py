#Start your python function here
def filtra_pares(a):
    pares=()
    if a[0] % 2 == 0:
        pares.append(a[0])
    if a[1] % 2 == 0:
        pares.append(a[1])
    return pares