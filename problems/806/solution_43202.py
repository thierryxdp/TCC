def colisao(a,b):
    x=str(a)
    y=str(b)
    if int(x[0] >= y[1:2]):
        return True
    elif int(x[0:1] <= y[0:1]):
        return False