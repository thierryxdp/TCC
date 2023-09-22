def colisao(a,b):
    x=str(a)
    y=str(b)
    if int(x[0:1])-int(y[0:1])<=-2:
        return 'True' 
    elif int(x[1:2])-int(y[1:2])<=-2:
        return 'True'