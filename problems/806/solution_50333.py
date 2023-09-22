def colisao(ret1, ret2):
    larg1 = ret1[2]-ret1[0]
    larg2 = ret2[2]-ret2[0]
    alt1 = ret1[3]-ret1[1]
    alt2 = ret2[3]-ret2[1]
    if ret1[0] < ret2[0]+larg2 and ret1[0]+larg1 > ret2[0] and ret1[1] < ret2[1]+alt2 and ret1[1]+alt1 > ret2[1]:
        return True
    else:
        return False