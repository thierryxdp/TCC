def filtra_pares(n1,n2,n3,n4):
    p1 = n1%2==0
    p2 = n2%2==0
    p3 = n3%2==0
    p4 = n4%2==0
    i1 = n1%2!=0
    i2 = n2%2!=0
    i3 = n3%2!=0
    i4 = n4%2!=0
    if n1%2==0:
        return (n1)