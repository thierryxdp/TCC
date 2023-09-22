#Start your python function here
def filtra_pares(x):
    pares = []
    for i in range(4):
        if x[i] % 2 == 0:
            pares.append(x[i])
    return tuple(pares)