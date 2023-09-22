#Start your python function here
def colisao(ret1,ret2):
    x1=ret1[0]
    x2=ret2[0]
    y1=ret1[1]
    y2=ret2[1]
    if x1>x2 and y1>y2 or y1<y2:
        return False
    if x1<x2 and y1>y2 or y1<y2:
        return False
    else:
        return True