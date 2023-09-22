def par(n):
    return (n % 2) == 0

def filtra_pares(t):
    ls = []
    if par(t[0]):
        list.append(ls, t[0])
    if par(t[1]):
        list.append(ls, t[1])
    if par(t[2]):
        list.append(ls, t[2])
    if par(t[3]):
        list.append(ls, t[3])
    return tuple(ls)