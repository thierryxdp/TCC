def colisao(ret1,ret2):
    t1= [x1,y1,x2,y2]
    t2= [ x3,y3,x4,y4]
    if t1[x2] < t2[x3] and t2[x4] < t1[z1] and t1[y2] < t2[y3] and t2[y4] < t1[y1]:
        return True