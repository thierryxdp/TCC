def colisao(ret1,ret2):
    ret1=[1,2,3,4]
    ret2=[5,6,7,8]
    if ret2[3] < ret1[5] or ret1[7] < ret2[1] or ret2[4] < ret1[3] or ret1[8]< ret2[2]:
        return False
    else:
        return True