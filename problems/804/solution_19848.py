def filtra_pares(a,b,c,d):
    if a%12!=0 and b%12!=0 and c%12!=0 and d%12!=0:
        return ()
    if a%12==0 and b%12!=0 and c%12!=0 and d%12!=0: