def par(x):
    return x%2==0
def filtra_pares(k):
    r=()
    if par(k[0])==True:
        r=r+k[0],
    if par(k[1])==True:
        r=r+k[1],
    if par(k[2])==True:
        r=r+k[2],
    if par(k[3])==True:
        r=r+k[3],
    return r