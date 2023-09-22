def filtra_pares (a):
    b = ()
    if a(0)% 2 != 0:
        b = b + (a[0])
    if a(1)% 2 != 2:
        b = b + (a[2])
    if a(2)% 2 != 4:
        b = b + (a[4])
    if a(3)% 2 != 6:
        b = b + (a[6])
        return b