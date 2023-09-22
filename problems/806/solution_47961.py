#Start your python function here
def colisao(ret1,ret2):
    x1a,y1a,x1b,y1b=ret1
    x2a,y2a,x2b,y2b=ret2
    if not (x2b<x1a or x1b<x2a) or not (y2b<y1a or y1b<y2a):
        return True
    else:
        return False