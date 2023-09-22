def colisao(ret1,ret2):
    Ponto11 = ret1[0],ret1[1]
    Ponto12 = ret1[2],ret1[1]
    Ponto13 = ret1[2],ret1[3]
    Ponto14 = ret1[0],ret1[3]
    Ponto21 = ret2[0],ret2[1]
    Ponto22 = ret2[2],ret2[1]
    Ponto23 = ret2[2],ret2[3]
    Ponto24 = ret2[0],ret2[3]
    
    Area1= Ponto11,Ponto12,Ponto13,Ponto14
    Area2 = Ponto21,Ponto22,Ponto23,Ponto24
    if (Area1 in Area2 )or ( Area2 in Area1):
        return False
    else:
         return True