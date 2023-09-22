#Start your python function here
def colisao(x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir,x_inf_esq1, y_inf_esq2,  x_sup_dir2, y_sup_dir):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''


    ret1 = (x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1) 
    ret2 = (x_inf_esq1, y_inf_esq2,  x_sup_dir2, y_sup_dir2)
    
    if ret1[2] < ret2[2] or ret2[2] < ret1[2] or ret1[3] < ret2[3] or ret2[3] < ret1[3]:
        return True 
    else:
        return False