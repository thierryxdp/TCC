def colisao(ret1,ret2):
    ret1 = ('x1','y1','x2','y2')
    ret2 = ('x3','y3','x4','y4')
    if (ret1[2]<ret2[0]) or (ret2[2]<ret1[0]) or (ret1[3]<ret2[1]) or (ret2[3]<ret1[3]):
        return 'False'
    else:
        return 'True'