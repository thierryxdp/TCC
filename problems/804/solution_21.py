def filtra_pares(a,b,c,d):
    A = a % 2
    B  = b % 2
    C = c % 2
    D = d % 2
    if not bool(A,B,C,D)==True:
        return (a,b,c,d)
    if not bool(A,B,C)==True:
        return (a,b,c)
    if not bool(A,B,D)==True:
        return (a,b,d)
    if not bool(A,C,D)==True:
        return (a,c,d)
    if not bool(B,C,D)==True:
        return (b,c,d)
    else:
        return ()