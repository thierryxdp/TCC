def filtra_pares(x):
    f=()
    if x[0]%2==0:
        f=f+(x[0],)
    if x[1]%2==0:
        f=f+(x[1],)
    if x[2]%2==0:
        f=f+(x[2],)
    if x[3]%2==0:
        f=f+(x[3],)
    return f