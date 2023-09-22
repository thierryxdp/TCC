#Start your python function here
def colisao(ret1,ret2):
    x11 = ret1[0]
    y11 = ret1[1]
    x12 = ret1[2]
    y12 = ret1[3]
    x21 = ret2[0]
	y21 = ret2[1]
    x22 = ret2[2]
    y22 = ret2[3]
    if x11 < x21 and x12 < x22:
        return True
    else: 
        return False