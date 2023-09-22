def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    r1,r2,r3,r4 = ret1
    R1,R2,R3,R4 = ret2
    if (r1 < R4) or (r2 < R3) or (r3 < R2) or (r4 < R1):
        return False
    else:
        return True