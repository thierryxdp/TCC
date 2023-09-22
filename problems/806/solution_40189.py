def colisao(ret1,ret2):
    Ponto11 = ret1[0],ret1[1]
    Ponto12 = ret1[2],ret1[1]
    Ponto13 = ret1[2],ret1[3]
    Ponto14 = ret1[0],ret1[3]
    Ponto21 = ret2[0],ret2[1]
    Ponto22 = ret2[2],ret2[1]
    Ponto23 = ret2[2],ret2[3]
    Ponto24 = ret2[0],ret2[3]
    

    if(rest1[2] < rest2[0])or(rest2[2] < rest1[0])or(rest1[3] < rest2[1])or(rest2[3] < rest1[1]):
        return False
    else:
         return True