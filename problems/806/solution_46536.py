#Start your python function here
import math
def colisao(ret1,ret2):
    D1=(ret1[2]-ret1[0])**2-(ret1[3]-ret1[1])**2
    D11=math.sqrt(D1)
    D2=(ret2[2]-ret2[0])**2-(ret2[3]-ret2[1])**2
    D22=math.sqrt(D2)
    return D1==D2