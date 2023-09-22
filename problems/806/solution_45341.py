def colisao(ret1,ret2):
    xinfe1,yinfe1,xsupd1,ysupd1 = ret1
    xinfe2,yinfe2,xsupd2,ysupd2 = ret2
    if xinfe1<=xinfe2<=xsupd1 and yinfe1<=ysupd2<=ysupd1:
        return True
    if xinfe2<=xinfe1<=xsupd1 and yinfe2<=ysupd1<=ysupd2:
        return True
    else:
        return False