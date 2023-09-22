def colisao(ret1,ret2):

    ret1 =tuple(ret1)
    ret2 =tuple(ret2)

    if (ret1[0] <= ret2[0] <= ret1[2] or ret1[0] <= ret2[2] < ret1[2]):
        return True
    else:
        return False