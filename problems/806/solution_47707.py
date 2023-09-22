def colisao(x,y):
    ''' Essa função recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se há colisão entre os 2 retângulos e False, caso contrário;
     tuple, tuple --> bool. '''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = x
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = y
    if x.intersection(y):
        return True
    else:
        return False