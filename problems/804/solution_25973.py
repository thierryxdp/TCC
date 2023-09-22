#Start your python function here
def pares (n):
    return n % 2 == 0
def filtra_pares (ls):
    return tuple (filtra (ls, pares))

def filtra (ls, p):
    r = [ ]
    for x in ls:
        if p (x):
            list.append (r, x)
    return r