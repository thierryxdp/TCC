def filtra_pares(t):
	a,b,c,d=t
    t2=()
    t3=()
    t4=()
    
    if type(a)%2==0:
        t2=t[0:1]+t2
    else:
        t3=t[0:1]+t3
    if type(b)%2==0:
        t2=t[1:2]+t2
    else:
        t3=t[1:2]+t3
    if type(c)%2==0:
        t2=t[2:3]+t2
    else:
        t3=t[2:3]+t3
    if type(d)%2==0:
        t2=t[3:]+t3
    else:
        t3=t[3:]+t3
    return a + b + c + d