def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
     intervalox1=(ret1[0], ret1[2])
    intervaloy1=(ret1[1],ret1[3])
    intervalox2=(ret2[0],ret2[2])
    intervaloy2=(ret2[1],ret2[3])
    if (intervalox1[0] not in range(intervalox2[0],intervalox2[1])) and ((intervalox1[1]) not in range(intervalox2[0],intervalox2[1])):
        return(False)
    
    elif (intervaloy1[0] not in range(intervaloy2[0],intervaloy2[1])) and ((intervaloy1[1]) not in range(intervaloy2[0],intervaloy2[1])):
        return(False)

    else:
        return True