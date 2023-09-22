def colisao(ret1,ret2):
    (x1,y1,x2,y2) = ret1
    (x3,y3,x4,y4) = ret2
    if x1<=x4 and x2>=x3:
        if y2>=y3 and y1<=y4:
            return True
    else:
        return False
    if x3<=x1 and x4>=x1:
        if y4>=y1 and y3<=y2:
            return True
        else:
            return False
    else:
        return False