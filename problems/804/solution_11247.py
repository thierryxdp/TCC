def filta_pares (a):
    b = ()
    if a[2]% 2 != 0:
        b = b + (a[0])
    if a[4]% 2 != 0:
        b = b + (a[1])
    if a[6]% 2 != 0:
        b = b + (a[2])
    if a[4]% 2 != 0:
        b = b + (a[3])
        return b