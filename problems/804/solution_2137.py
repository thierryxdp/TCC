def filtra_pares(t):
    '''tuple-->tuple'''
    i0=int(t[0])
    i1=int(t[1])
    i2=int(t[2])
    i3=int(t[3])
    if (i0%2==0) and (i1%2==0) and (i2%2==0) and (i3%2==0):
        return i0,i1,i2,i3
    elif (i0%2==0) and (i1%2==0) and (i2%2==0) and (i3%2!=0):
        return i0,i1,i2
    elif (i0%2==0) and (i1%2==0) and (i2%2!=0) and (i3%2!=0):
        return i0,i1
    elif (i0%2==0) and (i1%2!=0) and (i2%2!=0) and (i3%2!=0):
        return i0,
    elif (i0%2!=0) and (i1%2==0) and (i2%2==0) and (i3%2==0):
        return i1,i2,i3
    elif (i0%2!=0) and (i1%2!=0) and (i2%2==0) and (i3%2==0):
        return i2,i3
    elif (i0%2!=0) and (i1%2!=0) and (i2%2!=0) and (i3%2==0):
        return i3,
    elif (i0%2!=0) and (i1%2==0) and (i2%2==0) and (i3%2!=0):
        return i1,i2
    elif (i0%2==0) and (i1%2!=0) and (i2%2==0) and (i3%2!=0):
        return i0,i2
    elif (i0%2==0) and (i1%!=0) and (i2%!=0) and (i3%2==0):
        return i0,i3
    elif (i0%2!=0) and (i1%2==0) and (i2%2!=0) and (i3%2==0):
        return i1,i3
    else:
        return()