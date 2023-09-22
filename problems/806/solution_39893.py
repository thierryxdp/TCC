def colisão(retangulo1,retangulo2):
    x1=ret1[0]
    y1=ret1[1]
    x2=ret1[2]
    y2=ret1[3]
    x3=ret1[0]
    y3=ret2[1]
    x4=ret2[2]
    y4=ret2[3]
    if x<2<x3 or x4<x1 or y2<y3 or y4<y1:
        return False
    else:
        return True