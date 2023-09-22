def colisao(ret1,ret2):
    return not (ret2[2] < ret1[0] or ret1[2] < ret2[0]) and not (ret2[3] < ret1[1] or ret1[3] < ret2[1])