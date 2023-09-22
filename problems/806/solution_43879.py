#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
    xa1 =  x_inf_esq1
    ya1 =  y_inf_esq1
    xb1 =  x_sup_dir1
    yb1 =  y_sup_dir1
    xa2 =  x_inf_esq2
    ya2 =  y_inf_esq2
    xb2 =  x_sup_dir2
    yb2 =  y_sup_dir2
    if xa1 + (abs(xa1-xb1)) <= xa2 and ya1 + (abs (ya1-yb1)) <= ya2:
        return True
    else:
        return False