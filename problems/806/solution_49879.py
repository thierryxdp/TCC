#Start your python function here
def colisao(ret1,ret2):
    if ret2[2]>=ret1[0] and ret2[3]>=ret1[1]:
        return True
    else:
        return False