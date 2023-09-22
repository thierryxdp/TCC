def colisao([x1,y1,x2,y2],[x3,y3,x4,y4]):
    ret1 = (x1,y1,x2,y2)
    ret2 = (x3,y3,x4,y4)
    if x2<x3:
        if x4<x1:
            if y2<y3:
                if y4<y1:
                    return 'False'
                else:
                    return 'True'