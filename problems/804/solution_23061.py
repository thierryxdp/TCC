def par(x):
    if x%2 == 0:
        return x
    else:
        return 'ímpar'
    


def filtra_pares(a,b,c,d):
    r=()
    if eh_par(t[0]):
        r = r + (t[0])
    if eh_par(t[1]):
        r = r + (t[1],)
    if eh_par(t[2]):
        r = r + (t[2])
    if eh_par(t[3]):
        r = r + (t[3])
    else: 
        r = ()
    return r