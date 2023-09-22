def colisao(ret1,ret2):
    '''a função recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vértices: inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem. Devolvendo assim, True, se há colisão entre os 2 retângulos e False caso contrário.
     tuple, tuple --> bool'''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    x1=ret1[0]
    y1=ret1[1]
    x2=ret1[2]
    y2=ret1[3]
    x3=ret2[0]
    y3=ret2[1]
    x4=ret2[2]
    y4=ret2[3]
    if x2<x3 or x4<x1 or y2<y3 or y4<y1:
        return False
    else:
        return True