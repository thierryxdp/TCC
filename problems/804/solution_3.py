def filtra_pares(a,b,c,d):
    par = a/2%0 or b/2%0 or c/2%0 or d/2%0
    if not par:
        return 0