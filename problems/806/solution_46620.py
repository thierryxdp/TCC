def colisao(ret1,ret2):
    x=ret1[0]-ret1[2]
    x1=ret1[1]-ret1[3]
    z=ret2[0]-ret2[2]
    z1=ret2[1]-ret2[3]
    return x1!=z1 or x1==z1