#Start your python function here
def filtra_pares(t):
    t=(n1,n2,n3,n4)
    return t
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0:
        b=tuple(a)
        return b
    elif n1%2==0 and n2%2==0 and n3%2==0 and n4%2!=0:
        del a[3]
        b=tuple(a)
        return b
    elif n1%2==0 and n2%2==0 and n3%2!=0 and n4%2!=0:
        del a[3]
        del a[2]
        b=tuple(a)
        return b
    elif n1%2==0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
        del a[3]
        del a[2]
        del a[1]
        b=tuple(a)
        return b
    elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
        del a[3]
        del a[2]
        del a[1]
        del a[0]
        b=tuple(a)
        return b