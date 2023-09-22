#Start your python function here
def colisao(ret1,ret2):
    if ret1[0] < ret2[0] or ret2[0] < ret1[2] or ret1[1] < ret2[3] or ret2[1] < ret1[3] or ret1[0] > ret2[2] or ret2[0] > ret1[2] or ret1[1] > ret2[3] or ret2[0] > ret1[2]:
      	return False
    else:
       	return True