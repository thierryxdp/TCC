def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    reta1x=ret1[0],ret1[1]
    reta1y=ret1[2],ret1[3]
    reta2x=ret2[0],ret2[1]
    reta2y=ret2[2],ret2[3]
    if  reta1x>reta2x:
        if reta1y>reta2y:
            return True
    elif reta1x>reta2y:
         if reta1y>reta2x:
            return True
    else:
          return False