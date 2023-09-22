def filtra_pares(n1,n2,n3,n4):
    if n1%2 == 0:
        x = (n1,)
    else:
        x = ()
    if n2%2 == 0:
        y = (n2,)
    else:
        y = ()
    if n3%2 == 0:
        z = (n3,)
    else:
        z = ()
    if n4%2 ==0:
        w = (n4,)
    else:
        w = ()
        return x+y+z+w
        #Start your python function here