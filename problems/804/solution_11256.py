def filta_pares (a):
    b = ()
        if a[4]% 2 != 0:
            b = b + (a[4])
        if a[8]% 2 != 0:
            b = b + (a[8])
        if a[12]% 2 != 0:
            b = b + (a[12])
        if a[14]% 2 != 0:
            b = b + (a[14])
        return b