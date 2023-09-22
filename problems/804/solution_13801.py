a=tuple()
def filtra_pares(a):
    if a[0]%2==0:
        a=a+a[0]
    if a%2==0:
        a=a+a[1]
    if a%2==0:
        a=a+a[2]
    if a%2==0:
        a=a+a[3]
    return a