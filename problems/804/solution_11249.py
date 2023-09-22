def filta_pares (a):
    b = ()
    if a[4]% 2 != 0:
        b = b + (a[2])
    if a[8]% 2 != 0:
        b = b + (a[4])
    if a[12]% 2 != 0:
        b = b + (a[6])
    if a[14]% 2 != 0:
        b = b + (a[8])
        return b