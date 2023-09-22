#Start your python function here
def colisao(ret1,ret2):
      return ((ret1[2])<(ret2[0]))or((ret2[2])<(ret1[0]))or((ret1[3])<(ret2[1]))or((ret2[3])<(ret2[2]))or((ret2[0])>(ret1[2]))or((ret1[1])>(ret2[3]))or((ret2[1])>(ret1[3])