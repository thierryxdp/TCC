def filtra_pares(a):
    n1 = a[0]
    n2 = a[1]
    n3 = a[2]
    n4 = a[3]
    pares=( )
    if a[0] % 2 == 0:
        pares = pares + (a[0],)
    if a[1] % 2 == 0:
        pares = pares + (a[1],)
    if a[2] % 2 == 0:
        pares = pares + (a[2],)
    if a[2] % 2 == 0:
        pares = pares + (a[3],)
   		return pares