#Start your python function here
def colisao(rect1,rect2):
           xi=rect1[0]
           yi=rect1[1]
           xs=rect1[2]
           ys=rect1[3]
           xi2=rect2[0]
           yi2=rect2[1]
           xs2=rect2[2]
           ys2=rect2[3]
           l=xs-xi
           a=ys-yi
           l2=xs2-xi2
           a2=ys2-yi2
           if xi < xi2 + l2 and xi + l > xi2 and  yi < yi2 + a2 and yi + a > yi2:
             return 'True'
             else:
             return 'False'