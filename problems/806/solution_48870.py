#Start your python function here
def colisao(ret1,ret2):
    x1=ret1[0]
    x2=ret1[2]
    y1=ret1[1]
    y2=ret1[3]
    x3=ret2[0]
    x4=ret2[2]
    y4=ret2[1]
    y5=ret2[3]
   
    if x1<=x3 and x4 <=x2 or x1>=x3 and x4 >=x2 and y1<=y3 and y4 <=y2 or y1>= y3 and y4>=y2  
        return True
    else:
        return False