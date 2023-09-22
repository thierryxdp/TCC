def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    ret1=(x1,x2,y1,y2)
    ret2=(x3,x4,y3,y4)

    if x4<x1 or  x2<x3:
        xok= True
    else:
        xok= False
    if  y4<y1 or  y2< y3:
        yok= True
    else:
        yok= False
    if xok or yok:
        return False
    else:
        return True