def colisao(ret1,ret2):
    if ret1[0]>=ret2[0]:
        if ret1[1]>=ret2[1]:
            if ret2[2]>=ret1[0] and ret2[3]>=ret1[1]:
                return True
            else:
                return False
        else:
            if ret2[2]>=ret1[0] and ret1[3]>=ret2[1]:
                return True
            else:
                return False
        else:
        if ret1[1]>=ret2[1]:
            if ret1[2]>=ret2[0] and ret2[3]>=ret1[1]:
                return True
            else:
                return False
            else:
            if ret1[2]>=ret2[0] and ret1[3]>=ret2[1]:
                return True
            else:
                return False