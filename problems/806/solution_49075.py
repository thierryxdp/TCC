def colisao(ret1,ret2):

    #xesq yesq xdir ydir

    ret1 =tuple(ret1)
    ret2 =tuple(ret2)

    x1obj1 = ret1[0]
    y1obj1 = ret1[1]
    x2obj1 = ret1[2]
    y2obj1 = ret1[3]

    x1obj2 = ret2[0]
    y1obj2 = ret2[1]
    x2obj2 = ret2[2]
    y2obj2 = ret2[3]

    if x1obj1 <= x1obj2 <= x2obj1 or x1obj1 <= x2obj2 <= x2obj1:
        return True
    elif y1obj1 <= y1obj2 <= y2obj1 or y1obj1 <= y2obj2 <= y1obj1:
        return True
    else:
        return False