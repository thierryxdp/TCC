#Start your python function here
def colisao(ret1,ret2):
    x1,y1,x2,y2 = ret1
    x3,y3,x4,y4 = ret2
    if (x2 < x3):
        return "False"
    else:
        return "True"
    if (x4 < x1):
        return "False"
    else:
        return "True"
    if (y2 < y1):
        return "False"
    else:
        return "True"
    if (y4 < y1):
        return "False"
    else:
        return "True"