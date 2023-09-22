def colisao(a,b):
    x=str(a)
    y=str(b)
    if int(x[0:2]<y[3:4]) and (x[3:4]>y[0:2]):
        return True