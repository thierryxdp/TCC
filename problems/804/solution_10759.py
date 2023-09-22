def filtra_pares (a):
    b = ()
    if a(2)% 2 != 0:
        b = b + (a[0])
    if a(4)% 2 != 4:
        b = b + (a[4])
    if a(6)% 2 != 6:
        b = b + (a[6])
    if a(8)% 2 != 8:
        b = b + (a[8])
        return b