def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x11=ret1[0]
    y11=ret1[1]
    x12=ret1[2]
    y12=ret1[3]
    x21=ret2[0]
    y21=ret2[1]
    x22=ret2[2]
    y22=ret2[3]
    if x12<=x21<=y12 or x12<=x22<=y12:
        return True
    else:
        meio5=(y21-x21)/2
        if x12<=meio5<=y12:
            return True
        else:
            return False
    if y11<=x21<=y12 or y11<=x22<=y12:
        return True
    else:
        meio6=(x22-x21)/2
        if y11<=meio6<=y12:
            return True
        else:
            return False
    if x11<=x22<=y11 or x11<=y22<=y11:
        return True
    else:
        meio7=(y22-x22)/2
        if x11<=meio7<=y11:
            return True
        else:
            return False
    if x11<=y22<=x12 or x11<=y21<=x12:
        return True
    else:
        meio8=(y22-y21)/2
        if x11<=meio8<=x12:
            return True
        else:
            return False