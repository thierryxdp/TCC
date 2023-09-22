def filtra_pares(s):
    n1=s[0]
    n2=s[1]
    n3=s[2]
    n4=s[3]
    r1=n1%2
    r2=n2%2
    r3=n3%2
    r4=n3%2
    b1= (r1==0)
    b2= (r2==0)
    b3= (r3==0)
    b4= (r4==0)
    if b1 and b2 and b3 and b4:
        return tuple(s)
    elif not b1:
        if b2 and b3 and b4:
            return tuple(s[1:])
        if b2 and b3:
            return tuple(s[1:3])
        if b2 and b4:
            return tuple(s[1], s[3])
        if b3 and b4:
            return tuple(s[2], s[4])
        if b2:
            return tuple(s[1])
        if b3:
            return tuple (s[2])
        if b4:
            return tuple (s[3])