def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
     if max(ret1x1,ret1x2) < min(ret2x1,ret2x2) or max(ret2x1,ret2x2) < min(ret1x1,ret1x2) or max(ret1y1,ret1y2) < min(ret2y1,ret2y2) or max(ret2y1,ret2y2) < min(ret1y1,ret1y2):
            return False
        else:
            return True