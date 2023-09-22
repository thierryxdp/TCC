#Start your python function here
def colisao(ret1,ret2):
    [0,1,2,3] = ret1
    [4,5,6,7] = ret2
    if ret1[2] < ret2[4] or ret2[6] < ret1[0]\
    ret1[3]<ret2[5] or ret2[7] < ret1[1]:
        return False
    else: True