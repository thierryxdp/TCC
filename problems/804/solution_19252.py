#Start your python function here
#tupla-->tupla
def filtra_pares (t):
    if t[0]%2 == 0:
        t = t[1:4]
        return t
    else:
        return t