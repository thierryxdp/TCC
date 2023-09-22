#Start your python function here
def colisao(ret1,ret2):
    if ret1[2] < ret2[0] or ret2[2] < ret1[0] or ret1[3] < ret2[1] or ret2[3] < ret1[1]:
        return False
    else:
        return True