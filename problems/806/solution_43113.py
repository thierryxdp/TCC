def colisao(a,b):
    x=str(a)
    y=str(b)
    if int(x > y):
        return True
    elif int (x <= y):
        return False
    elif int(x[0:2] >= y[3:5]) and int (x[3:5] <= y[0:2]):
        return False