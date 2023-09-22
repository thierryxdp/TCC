def colisao(ret1,ret2):
    if ret1[1]>ret2[3] or ret1[2]<ret2[0] or ret1[3]<ret2[1] or ret1[0]>ret2[2]:
        return False
    else:
        return True