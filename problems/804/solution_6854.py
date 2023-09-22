def filtra_pares(a):
    x=()
    if a[0]%2==0:
        x=x+tuple((a[0],))
        return x
    if a[1]%2==0:
        x=x+tuple((a[1],))
        return x
    if a[2]%2==0:
        x=x+tuple((a[2],))
        return x
    if a[3]%2==0:
        x=x+tuple((a[3],))
        return x