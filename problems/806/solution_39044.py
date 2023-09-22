def colisao(ret1,ret2):
    if ret1[2]< ret2[4] or ret2[6] or ret1[0]:
        return True
    else:
        return False