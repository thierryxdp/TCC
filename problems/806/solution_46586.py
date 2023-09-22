def colisao(ret1,ret2):
    D1=(ret1[2]-ret1[0])**2-(ret2[2]-ret2[0])**2
    D11=D1
    D2=(ret1[3]-ret1[1])**2-(ret2[3]-ret2[1])**2
    D22=D2
    if D11!=D22:
        return True
    else:
        return True
    else:
        return False