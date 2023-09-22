def colisao(ret1,ret2):
    if ret1[0]==ret2[0]:
        return 4==4
    elif ret1[2]==ret2[2] and ret1[0]==1:
        return 4==4
    elif ret1[2]==ret2[2] and not ret1[1]==ret2[1]:
        return 4==5