def colisao(ret1,ret2):
    ret1=[1,2,3,4]
    ret2=[5,6,7,8]
    if ret1[3] < ret2[5] or ret2[7] < ret1[1] or ret1[4] < ret2[3]:
        return False
    else:
        return True