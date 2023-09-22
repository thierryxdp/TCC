def colisao(a,b):
    x=str(a)
    y=str(b)
    if int(x[2:5] > y[2:5]) and int(x[0:2] > y[0:2]):
        return False
    elif int (x[2:5] < y[0:2]) and int(x[0:2] > y[2:5]):
        return True