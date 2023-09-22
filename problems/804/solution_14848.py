def filtra_pares(a):
    b=()
    if a[0]%2==0:
        b=(a[0],)
    elif a[1]%2==0:
        b=b+(a[1],)
    elif a[2]%2==0:
        b=b+(a[2],)
    elif a[3]%2==0:
        b=b+(a[3],)
    return b