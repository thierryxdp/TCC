def filtra_pares(a):
    x=()
    y=()
    z=()
    k=()
    p=()
    if a[0]%2==0:
        x=a[0]
        p=x
    if a[1]%2==0:
        y=a[0] 
        p=p,y
    if a[2]%2==0:
        z=a[0]
        p=p,z
    if a[3]%2==0:
        k=a[0]
        p=p,k
    return p