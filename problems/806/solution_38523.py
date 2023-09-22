#Start your python function here
def colisao(ret1,ret2):
    if((ret1[0],ret1[1])<=(ret2[0],ret2[1]))and((ret1[2],ret1[3])<=(ret2[2],ret2[3]))or((ret1[0],ret1[1])>=(ret2[0],ret2[1]))and((ret1[2],ret1[3])>=(ret2[2],ret2[3])):
        return True
    else:
                return False