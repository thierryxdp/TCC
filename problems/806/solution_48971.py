def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    if ret1[2:]==ret2[2:]:
        return True
    if len(ret1[2])-len(ret2[2])==1 and len(ret1[3])-len(ret2[3])==1:
        return True
    if len(ret1[2])-len(ret2[2])==2 and len(ret1[3])-len(ret2[3])==2:
        return True
    if len(ret1[2])-len(ret2[2])==2 and len(ret1[3])-len(ret2[3])==1:
        return True
    if len(ret1[2])-len(ret2[2])==1 and len(ret1[3])-len(ret2[3])==2:
        return True
    else:
        len(ret1[2:])-len(ret2[2:])>2
        return False