def  filtra_pares(a):
    pares=[]
    if a[0]%2==0:
        pares.insert(0,a[0])
    if a[1]%2==0:
        pares.insert(1,a[1])
    if a[2]%2==0:
        pares.insert(2,a[2])
    if a[3]%2==0:
        pares.insert(3,a[3])
    return tuple(pares)