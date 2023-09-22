def filtra_pares(a):
    z=()
    if a[0]%2==0:
        z=z+(a[0],)
    if a[1]%2==0:
        z=z+(a[1],)
    if a[2]%2==0:
        z=z+(a[2],)
    if a[3]%2==0:
        z=z+(a[3],)
    return z