def filtra_pares(t):
    if ((t[0])%2==0) or ((t[1])%2==0):
        a1 = 0;
        if ((t[0])%2==0)and((t[1])%2==0):
            a = (t[0],t[1])
        elif (t[0])%2==0:
                a = (t[0],)
        else:
                a = (t[1],)
    else:
        a1 = 1
    
    if ((t[2])%2==0)or ((t[3])%2==0):
        b1 = 0
        if ((t[2])%2==0)and((t[3])%2==0):
            b = (t[2],t[3])
        elif (t[2])%2==0:
            b = (t[2],)
        else:
            b = (t[3],)
    else:
        b1 = 1

    print (a1,b1, '')

    if ((a1 == 0 )and (b1 == 0)):
        return a[:] + b[:]
    else:
        if (a1 == 0):
            return a[:]
        else:
            if (b1 == 0):
                return b[:]
            else:
                return ""