def filtra_pares(s):
    n1=s[0]
    n2=s[1]
    n3=s[2]
    n4=s[3]
    r1=n1%2
    r2=n2%2
    r3=n3%2
    r4=n4%2
    b1= (r1==0)
    b2= (r2==0)
    b3= (r3==0)
    b4= (r4==0)
    if b1:
        if b2:
            if b3:
                if b4:
                    return tuple(s)
                else:
                    return tuple (s[:3])
            else:
                if b4:
                    return tuple(s[0], s[1], s[3])
                else:
                    return tuple (s[:2])
        else:
            if b3:
                if b4:
                    return (s[0] , s[2] , s[3])
                else:
                    return tuple (s[0],s[2])
            else:
                if b4:
                    return tuple(s[::3])
                else:
                    return tuple (s[:1])
    else:
        if b2:
            if b3:
                if b4:
                    return tuple(s[1:])
                else:
                    return tuple(s[1:3])
            else:
                if b4:
                    return tuple(s[1:1:-2])
                else:
                    return tuple(s[2::3])
        else:
            if b3:
                if b4:
                    return tuple(s[2:1:-2])
                else:
                    return tuple(s[2:3])
            else:
                if b4:
                    return (s[3])
                else:
                    return tuple()