def d(x):
    return x%2==0
def filtra_pares(a,b,c,d):
    if d(a)==d(b)==d(c)==d(d)==True:
        return a,b,c,d
    if d(a)==d(b)==d(c)==True and d(d)==False:
        return a,b,c
    if d(a)==d(b)==True and d(c)==d(d)==False:
        return a,b
    if d(a)==d(c)==True and d(b)==d(d)==False:
        return a,c
    if d(a)==True and d(b)==d(c)==d(d)==False:
        return a
    if d(a)==d(b)==d(d)==True and d(c)==False:
        return a,b,d
    if d(a)==d(c)==d(d)==True and d(b)==False:
        return a,c,d
    if d(a)==d(d)==True and d(b)==d(c)==False:
        return a,d
    if d(b)==True and d(a)==d(c)==d(d)==False:
        return b
    if d(c)==True and d(a)==d(b)==d(d)==False:
        return c
    if d(d)==True and d(a)==d(b)==d(c)==False:
        return d
    if d(a)==False and d(b)==d(c)==d(d)==True:
        return b,c,d
    if d(a)==d(b)==False and d(c)==d(d)==True:
        return c,d
    if d(a)==d(c)==False and d(b)==d(d)==true:
        return b,d
    if d(a)==d(d)==False and d(b)==d(c)==True:
        return b,c
    else:
        return