def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xinfa, yinfa, xsupa, ysupa = ret1
    xinfb, yinfb,  xsupb, ysupb = ret2
    if xsupb < xinfa or xsupa < xinfb
        xintercep = True
    else:
        xintercep = False
    if y_sup_dir2 < y_inf_esq1 or y_sup_dir1 < y_inf_esq2
        yintercep = True
    else:
        yintercep = False
    if xintercep or yintercep:
        return False
    else:
        return True