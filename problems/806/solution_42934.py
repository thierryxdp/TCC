def colisao(a,b):
    from math import abs
    x1=int(a[0:1]
    y1=int(a[1:2]
    X1=int(a[2:3]
    Y1=int(a[3:4]
    x2=int(b[0:1]
    y2=int(b[1:2]
    X2=int(b[2:3]
    Y2=int(b[3:4]
    if abs((x1,y1,X1,Y1)-(x2,y2,X2,Y2))>=2:
           return 'True'