#Start your python function here
def colisao(ret1,ret2):
    x1=ret1[0]
    x2=ret2[0]
    y1=ret1[1]
    y2=ret2[1]
    if x1<=x<=x2 and y1<=y<=y2:
        return True
    else:
        return False