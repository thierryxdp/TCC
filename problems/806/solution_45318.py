#Start your python function here
def colisao(ret1,ret2):
    xinfe1,yinfe1,xsupd1,ysupd1 = ret1
    xinfe2,yinfe2,xsupd2,ysupd2 = ret2
    if xsupd1 >= xinfe2 | xsupd1>= yinfe2:
        saida = True
    else:
        saida = False
        return saida