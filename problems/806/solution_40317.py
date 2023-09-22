def colisao(ret1,ret2):
    retA=((ret1)[0:1](ret1)[1:2](ret1)[2:3](ret1)[3:4])
    retB=((ret2)[0:1](ret2)[1:2](ret2)[2:3](ret2)[3:4])
    if retA in retB:
        return True
    else:
        return False