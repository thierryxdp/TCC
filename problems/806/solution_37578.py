#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    tuple(ret1)
    tuple(ret2)
    x_inf_esq1=int(ret1[0])
    y_inf_esq1=int(ret1[2])
    x_sup_dir1=int(ret1[4])
    y_sup_dir1=int(ret1[6])
    x_inf_esq2=int(ret2[0])
    y_inf_esq2=int(ret2[2])
    x_sup_dir2=int(ret2[4])
    y_sup_dir2=int(ret2[6])
    
    if x_inf_esq1>=x_sup_dir2 and y_inf_esq1>y_sup_dir2:
        return False
    if x_inf_esq1>=x_sup_dir2 and y_sup_dir1<y_inf_esq2:
        return False
    if x_sup_dir1<=x_inf_esq2 and y_sup_dir1<y_inf_esq2:
        return False
    if x_inf_esq1<=x_inf_esq2 and y_sup_dir1>y_inf_esq2:
        return False
    else:
        return True

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado