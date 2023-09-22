#Start your python function here
def colisao(ret1,ret2):
      '''ret1(x1,y1),(x2,y2)  ret2(x3,y3),(x4,y4)'''
      if ret1[0] >= ret2[0] and ret1[0] <= ret2[2] and ret1[1] >= ret2[1] and ret1[1] <= ret2[3]:
            return True
      elif ret1[2] >= ret2[0] and ret1[2] <= ret2[2] and ret1[3] >= ret2[1] and ret1[3] <= ret2[3]:
            return True
      else:
            return False