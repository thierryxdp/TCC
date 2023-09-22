#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    
    reta1_1 = tuple(x_inf_esq1, y_inf_esq1)
    reta1_2 = tuple(x_sup_dir1, y_sup_dir1)
    reta2_1 = tuple(x_inf_esq2, y_inf_esq2)
    reta2_2 = tuple(x_sup_dir2, y_sup_dir2)
   
    if reta1_1<=reta2_1:
        return "True"
    elif reta1_2<=reta2_1:
        return "True"
    else:
        return "False"