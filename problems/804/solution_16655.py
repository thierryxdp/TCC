def filtragem_pares(x,w,y,z):
    a = x%2
    b = w%2
    c = y%2
    d = z%2
    if a==b==c==d==0:
        return x,w,y,z
    elif a==b==c==0:
        return x,w,y
    elif a==b==d==0:
        return x,w,z
    elif b==c==d==0:
        return w,y,z
    elif a==d==0:
        return x,z
    elif a==b==0:
        return x,w
    elif a==c==0:
        return x,y
    elif b==d==0:
        return w,z
    elif b==c==0:
        return w,y
    elif c==d==0:
        return y,z
    elif a==0:
        return x
    elif b==0:
        return w
    elif c==0:
        return y
    elif d==0:
        return z
    elif (a!=0)  and  (b!=0) and  (c!=0) and(d!=0):
        return ''