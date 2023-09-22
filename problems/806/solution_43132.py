def colisao(a,b):
    x=str(a)
    y=str(b)
    if int(x[2:4]> y[0:2]) and int(x[0:2]< y[2:4]):
        return True
    elif int (x[2:4]< y[0:2]) and int(x[0:2]< y[2:4]):
        return False