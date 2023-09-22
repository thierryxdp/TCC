def d(x):
    return x%2==0
def f(a,b,c,d):
    if d(a)==d(b)==d(c)==d(d)==True:
        return a,b,c,d
    elif d(a)==d(b)==d(c)==True and d(d)==False:
        return a,b,c
    elif d(a)==d(b)==True and d(c)==d(d)==False:
        return a,b
    elif d(a)==d(c)==True and d(b)==d(d)==False:
        return a,c
    elif d(a)==True and d(b)==d(c)==d(d)==False:
        return a,
    elif d(a)==d(b)==d(d)==True and d(c)==False:
        return a,b,d
    elif d(a)==d(c)==d(d)==True and d(b)==False:
        return a,c,d
    elif d(a)==d(d)==True and d(b)==d(c)==False:
        return a,d
    elif d(b)==True and d(a)==d(c)==d(d)==False:
        return b,
    elif d(c)==True and d(a)==d(b)==d(d)==False:
        return c,
    elif d(d)==True and d(a)==d(b)==d(c)==False:
        return d,
    elif d(a)==False and d(b)==d(c)==d(d)==True:
        return b,c,d
    elif d(a)==d(b)==False and d(c)==d(d)==True:
        return c,d
    elif d(a)==d(c)==False and d(b)==d(d)==true:
        return b,d
    elif d(a)==d(d)==False and d(b)==d(c)==True:
        return b,c
    else:
        return