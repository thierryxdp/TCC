#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xa1=x_inf_esq1, ya1=y_inf_esq1, xa2=x_sup_dir1, ya2=y_sup_dir1 = ret1
    xb1=x_inf_esq2, yb1=y_inf_esq2, xb2=x_sup_dir2, yb2=y_sup_dir2 = ret2
    if xb1>xa2 and yb1<ya2 or yb1>ya2 and xb1<xa2 or yb2<ya1 and xb1<xa2:
        return False
    else:
        return True