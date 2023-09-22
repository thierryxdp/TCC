#Start your python function here
def filtra_pares(x):
    for i in range(4):
        pares = ()
        if x[i] % 2 == 0:
            pares.append(x[i])
    return tuple(pares)