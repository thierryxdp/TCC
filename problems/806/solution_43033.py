def colisao(a,b):
    x=str(a)
    y=str(b)
    if int(x[0:2] <= y[0:2]!=1) and (x[2:4] <= y[2:4]!=1):
        return True 
    else:
        return False