#Start your python function here
import math
def colisao(ret1,ret2):
    x11 = ret1[0]
    y11 = ret1[1]
    x12 = ret1[2]
    y12 = ret1[3]
    x21 = ret2[0]
    y21 = ret2[1]
    x22 = ret2[2]
    y22 = ret2[3]
    math.abs(y22 - y11) = d_total_y
    math.abs(y11 - y12) = yq1
    math.abs(y21 - y22) = yq2
    math.abs(x22 - x11) = d_total_x
    math.abs(x11 - x12) = xq1
    math.abs(x21 - x22) = xq2
    if yq1 + yq2 >= d_total_y and xq1 + xq2 >= d_total_x:
      	return True
    else:
       	return False