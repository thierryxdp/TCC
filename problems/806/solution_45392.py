def colisao(ret1,ret2):
    ret1=(x1,y1,x2,y2)
    ret2=(x3,y3,x4,y4)
    if ret1[0]>ret2[2]and ret2[0]>ret1[2] or ret2[3]<ret[1]or ret1[3]<ret2[1]:
        return False