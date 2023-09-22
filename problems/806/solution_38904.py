#Start your python function here
def colisao(ret1,ret2):
    dinf=((ret1(0)-ret2(0))**2+(ret1(1)-ret2(1))**2)*1/2
    dsup=((ret1(2)-ret2(2))**2+(ret1(3)-ret2(3))**2)*1/2
    if dinf or dsup > 0:
        return false
    else:
        return true