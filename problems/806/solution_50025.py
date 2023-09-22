#Start your python function here
def colisao(ret1,ret2):
    x11 = ret1[0]
    y11 = ret1[1]
    x12 = ret1[2]
    y12 = ret1[3]
    x21 = ret2[0]
    y21 = ret2[1]
    x22 = ret2[2]
    y22 = ret2[3]
    if abs(y21 - y12) < abs(y22 - y11):
      d_total_y = abs(y22 - y11)
    else:
      d_total_y = abs(y21 - y12)
    if abs(x21 - x12) < abs(x22 - x11):
      d_total_x = abs(x22 - x11)
    else:
      d_total_x = abs(x21 - x12)
    yq1 = abs(y11 - y12)
    yq2 = abs(y21 - y22)
    d_total_x = abs(x22 - x11)
    xq1 = abs(x11 - x12)
    xq2 = abs(x21 - x22)
    print(yq1)
    print(yq2)
    print(d_total_y)
    if yq1 + yq2 >= d_total_y and xq1 + xq2 >= d_total_x:
      	return True
    else:
       	return False