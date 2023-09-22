def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    s1=x_sup_dir1-x_inf_esq2
    s2=y_sup_dir1-y_inf_esq2
    s3=x_sup_dir2-x_inf_esq1
    s4=y_sup_dir2-y_inf_esq1

    ladoa1=range(y_inf_esq1,y_sup_dir1+1)
    ladoa2=range(y_inf_esq2,y_sup_dir2+1)

    ladob1=range(x_inf_esq1,x_sup_dir1+1)
    ladob2=range(x_inf_esq2,x_sup_dir2+1)

    if  ((x_sup_dir1>=x_inf_esq2 and (y_sup_dir2 in ladoa1 or y_inf_esq2 in ladoa1)) or (y_inf_esq1<=y_sup_dir2 and (x_sup_dir2 in ladob1 or x_inf_esq2 in ladob1)) or (x_inf_esq1<=x_sup_dir2 and (y_sup_dir2 in ladoa1 or y_inf_esq2 in ladoa1)) or (y_sup_dir1>=y_inf_esq2 and (x_inf_esq2 in ladob1 or x_sup_dir2 in ladob1)))and x_sup_dir1==x_inf_esq2 or y_sup_dir1==y_inf_esq2 or x_inf_esq1==x_sup_dir2 or y_inf_esq1==y_sup_dir2:                                                                                                                                                                                                   
        return True
    if s1>0 and s2>0 and s3>0 and s4>0 and((x_sup_dir1-s1)==x_inf_esq2 or (y_sup_dir1-s2)==y_inf_esq2 or (x_inf_esq1-s3)==x_sup_dir2 or (y_inf_esq1-s4)==y_sup_dir2):
        return True
    else:
        return False