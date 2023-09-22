def filtro(t):
    result = ()
    i0=int(t[0])
    i1=int(t[1])
    i2=int(t[2])
    i3=int(t[3])
    if i0%2==0:
        result= result + (i0,)
    if i1%2==0:
        result= result + (i1,)
    if i2%2==0:
        result= result + (i2,)
    if i3%2==0:
        result= result + (i3,)
    return result