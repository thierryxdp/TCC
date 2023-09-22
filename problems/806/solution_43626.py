def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    a, b, c, d = x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1
    x, y, z, w = x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2

    if ((x<=a<=z and y<=b<=w)or(x<=c<=z and y<=d<=w))or((a<=x<=c and b<=y<=d)or(a<=z<=c and b<=w<=d)):
        return True
    else:
        return False