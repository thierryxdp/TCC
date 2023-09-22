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
   
    if x1>x4 and y1>y4 or y1<y4:  
        return False
    if x2<x3 and y2>y3 or y2<y3:
    	return False
    else:
        return True