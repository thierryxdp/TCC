def colisao(ret1,ret2):
    xinfe1,yinfe1,xsupd1,ysupd1 = ret1
    xinfe2,yinfe2,xsupd2,ysupd2 = ret2
    if xinfe1<=xinfe2<=xsupd1 or yinfe1<=ysupd2<=ysupd1:
        return True
    else:
        return False