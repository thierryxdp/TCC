def colisao(ret1,ret2):
    if ret1[2]<ret2[0]:
        return False
    elif ret2[2]<ret1[0]:
        return False
    elif ret1[3]<ret2[1]:
        return True