def colisao(ret1,ret2):

 if ((ret1[1]>=ret2[1] and ret1[1]<=ret2[3]) or (ret2[1]>=ret1[1] and ret2[1]<=ret1[3])) and ((ret2[0]<=ret1[0] and ret1[0]<=ret2[2])or(ret1[0]<=ret2[0] and ret2[0]<=ret1[2])):
  return True
 else:
  return False