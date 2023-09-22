#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1= ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2= ret2
    ret1_x = ret1[:1]
    ret1_y = ret1[2:3]
    ret1_w = ret1[4:5]
    ret1_h = ret1[6:7]
    ret2_x = ret2[:1]
    ret2_y = ret2[2:3]
    ret2_w = ret2[4:5]
    ret2_h = ret2[6:7]
    
    if (ret1_x<=ret2_x+ret2_w and ret1_x+ret1_w>=ret2_x)and(ret1_y<=ret2_y+ret2_h and ret1_y+ret1_h>=ret2_y):
        return True
    else:
        return False