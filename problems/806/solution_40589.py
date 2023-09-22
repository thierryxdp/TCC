def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xla,yla, x2a,y2a = ret1
    xlb,ylb, x2b,y2b = ret2
    if xb2 < xla or x2a < xlb:
        xok = True
    else:
        xok = False
    if y2b < yla or y2a < ylb:
        yok = True
    else:
        yok = False
    if xok or yok:
        return False
    else:
        return True