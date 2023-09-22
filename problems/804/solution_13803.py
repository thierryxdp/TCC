a=tuple()
def filtra_pares(a):
    if a[0]%2==0:
        a=a+a
    if a[1]%2==0:
        a=a+a
    if a%2==0:
        a=a+a[2]
    if a%2==0:
        a=a+a[3]
    return a