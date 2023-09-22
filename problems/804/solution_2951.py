def filtra_pares(a,b,c,d):
    if a%2==0 and (not b%2==0 and not c%2==0 and not d%2==0):
        return a
    elif b%2==0 and (not a%2==0 and not c%2==0 and not d%2==0):
        return b
    elif c%2==0 and (not a%2==0 and not b%2==0 and not d%2==0):
        return c
    elif d%2==0 and (not b%2==0 and not c%2==0 and not a%2==0):
        return d
    elif a%2==0 and b%2==0 and (not c%2==0 and not d%2==0):
        return a,b