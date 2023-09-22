def filtra_pares(tupla):
    a= tupla[0]
    b= tupla[1]
    c=tupla[2]
    d=tupla[3]
    if a/2 and b/2 and c/2 and d/2==int:
        return a,b,c,d
    elif a/2 and b/2 and c/2==int:
        return a,b,c
    elif a/2 and b/2==int:
            return a,b
    elif a/2==round:
        return a
    elif b/2 and c/2 and d/2== int:
        return b,c,d
    elif b/2 and c/2:
        return b,c
    elif b/2:
        return b
    elif c//2 and d//2:
        return c,d
    elif a//2 and b//2 and d//2:
        return a,b,d
    elif c//2 and d//2 and a//2:
        return c,d,a