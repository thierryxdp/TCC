def num_par(n):
    return n%2==0
def filtra_pares(t):
    r=()
    if num_par(t[0]):
        r = r+(t[0])
    if num_par(t[1]):
        r = r + (t[1])
    if num_par(t[2]):
        r = r + (t[2])
    if num_par(t[3]):
        r = r + (t[3])
    return r