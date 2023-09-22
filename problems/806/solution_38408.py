#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    
    ret1x=ret1[:1]
    ret1y=ret1[2:3]
    ret1w=ret1[4:5]
    ret1h=ret1[6:7]
    ret2x=ret2[:1]
    ret2y=ret2[2:3]
    ret2w=ret2[4:5]
    ret2h=ret2[6:7]
    if ret1x<ret2x+ret2w and ret1x+ret1w>ret2x and ret1y<ret2y+ret2h and ret1y+ret1h>ret2y:
        return True
    else:
        return False