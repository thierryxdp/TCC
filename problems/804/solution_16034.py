def filtra_pare(a,b,c,d):
    if par(a)and par(b)and par(c)==True and par(d)==False:
        return a,b,c
    elif par(b)and par(c)and par(d)==True and par(a)==False:
        return b,c,d
    elif par(a)and par(c)and par(d)==True and par(b)==False:
        return a,c,d
    elif par(c)and par(d)==True and par(a) and par(b)==False:
        return c,d
    elif par(a)and par(b)and(d)==True and par(c)==False:
        return a,b,d
    elif par(a)and par(c)==True and par(b) and par(d)==False:
        return a,c
    elif par(a) and par(b) and par(c) and par(d)==True:
        return a,b,c,d
    elif par(b)and par(d)==True and par(c) and par(a)==False:
        return b,d
    elif par(a)and par(b)==True and par(c) and par(d)==False:
        return a,b
    elif par(a)and par(d)==True and par(b) and par(c)==False:
        return a,d
    elif par(c)and par(b)==True and par(a) and par(d)==False:
        return c,b