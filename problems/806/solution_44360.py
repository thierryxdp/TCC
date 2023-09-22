#Start your python function here
def colisao(ret1,ret2):
    
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool
     '''
    #ret1
    x1=ret1[0]
    y1=ret1[1]
    x2=ret1[2]
    y2=ret1[3]
    #ret2
    x3=ret2[0]
    y3=ret2[1]
    x4=ret2[2]
    y4=ret2[3]
    
    if x3<=x1 and x1<=x4 and y3<=y1 and y1<=y4:
        return true
    elif x3<=x2 and x2<=x4 and y3<=y2 and y2<=y4:
        return true
    elif  x1<=x3 and x3<=x2 and y1<=y3 and y3<=y2:
        return true
    elif  x1<=x4 and x4<=x2 and y1<=y4 and y4<=y2:
        return true
    else:
        return false