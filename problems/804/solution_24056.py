#Start your python function here
def filtra_pares(k):
    t=()
    if k[0]%2 == 0:
        aux = k[0]
        t = t + (aux,)
    if k[1]%2 == 0:
        aux = k[1]
        t = t + (aux,)
    if k[2]%2 == 0:
        aux = k[2]
        t = t + (aux,)
    return t