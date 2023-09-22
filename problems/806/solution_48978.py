def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if ret1[2:]==ret2[2:]:
        return True
    if abs(ret1[2]-ret2[2])==1 and abs(ret1[3]-ret2[3])==1:
        return True
    if abs(ret1[2]-ret2[2])==2 and abs(ret1[3]-ret2[3])==2:
        return True
    if abs(ret1[2]-ret2[2])==2 and abs(ret1[3]-ret2[3])==1:
        return True
    if abs(ret1[2]-ret2[2])==1 and abs(ret1[3]-ret2[3])==2:
        return True
    if ret1[2]==ret2[2] and abs(ret1[3]-ret2[3])==2:
        return True
    if abs(ret1[2]-ret2[2])==1 and ret1[3]==ret2[3]:
        return True
    if ret1[2]==ret2[2] and abs(ret1[3]-ret2[3])==1:
        return True
    if abs(ret1[2]-ret2[2])==2 and (ret1[3]==ret2[3]:
        return True
    else:
        if abs(ret1[2]-ret2[2])>2:
        	return False
        if abs(ret1[3]-ret2[3])>2:
            return False