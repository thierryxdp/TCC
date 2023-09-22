def colisao(ret1,ret2):
    Ponto11 = ret1[0],ret1[1]
    Ponto12 = ret1[2],ret1[1]
    Ponto13 = ret1[2],ret1[3]
    Ponto14 = ret1[0],ret1[3]
    Ponto21 = ret2[0],ret2[1]
    Ponto22 = ret2[2],ret2[1]
    Ponto23 = ret2[2],ret2[3]
    Ponto24 = ret2[0],ret2[3]
    

    if(ret1[2] < ret2[0])or(ret2[2] < ret1[0])or(ret1[3] < ret2[1])or(ret2[3] < ret1[1]):
        return False
    else:
         return True