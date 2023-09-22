def filtra_pares(s):
    z=int(s)[:1]+int(s)[1:2]+int(s)[2:3]+int(s)[3:]
    a= list(z)
    y= ''.join(a) # converting list into string
    x=int(y)
    return x*2