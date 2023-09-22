def filtra_pares(a):
    pares_novo=(0,)
    if a[0]%2==0:
        pares_novo.insert(0,a[0])
    if a[1]%2==0:
        pares_novo.insert(1,a[1])
    if a[2]%2==0:
        pares_novo.insert(2,a[2])
    if a[3]%2==0:
        pares_novo.insert(3,a[3])
    return pares_novo