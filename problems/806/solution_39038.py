def colisao(ret1,ret2):
    ret1 = [0,1,2,3]
    ret2= [ 4,5,6,7]
    if ret1[2] == ret2[4] and ret2[6] == ret1[4] and ret1[3] == ret2[5] and ret2[7] == ret1[1]:
        return True