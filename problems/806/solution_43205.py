def colisao(a,b):
    x=str(a)
    y=str(b)
    if int(x[0:1] < y[0:1]):
        return False
    elif int(x[3:4] < y[0:1]):
        return True