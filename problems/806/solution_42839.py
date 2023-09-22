def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    """x_inf_esq1= canto inferior esquerdo na coordenada x do retangulo 1, y_if_esq1=canto inferior esquerdo na coordena y do retangulo 1, x_sup_dir1= canto superior direito na coordenada x do retângulo 1,y_sup_dir1+ canto superior direito na coordenada y do retângulo 1. Seguir o mesmo raciocínio para o retângulo 2, substituindo o 1 de cada variável por 2"""

    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if y_inf_esq2<=y_sup_dir1<=y_sup_dir2 and x_inf_esq1<=x_sup_dir2<=x_sup_dir1:
        return True
    else:
        if y_inf_esq2<=y_inf_esq1<=y_sup_dir2 and x_inf_esq1<=x_inf_esq2<=x_sup_dir1:
            return True
        else:
            return False