#Start your python function here
def colisao(ret1,ret2):
   x1 = ret1[1]
   y1 = ret1[2]
   x2 = ret2[1]
   y2 = ret2[2]
   if x1 == x2 and y1 == y2:
      return True
   else:
      return False