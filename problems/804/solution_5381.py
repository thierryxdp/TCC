def filtra_pares(a):
    x=a[1]%2==0
    y=a[2]%2==0
    z=a[3]%2==0
    w=a[4]%2==0
    if x and y and z and w:
        return a