def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    
    if (ret1[3])<(ret1[0]) or  (ret1[1])<(ret1[2]):
        xok= True
    else:
        xok= False
    if  (ret2[3])<(ret2[0]) and  (ret2[1])<(ret2[2]):
        yok= True
    else:
        yok= False
    if xok or yok:
        return False
    else:
        return True