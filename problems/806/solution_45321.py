#Start your python function here
def colisao(ret1,ret2):
    xinfe1,yinfe1,xsupd1,ysupd1 = ret1
    xinfe2,yinfe2,xsupd2,ysupd2 = ret2
    if xinfe1<xinfe2<xsup1 and yinfe1<ysup2<ysup1:
        return True
    else:
        return False