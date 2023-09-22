#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    x1,y1=x_inf_esq1,y_inf_esq1
    x3,y3= x_sup_dir1,y_sup_dir1
    x2,x2=x_inf_esq2, y_inf_esq2
    x4,y4=x_sup_dir2, y_sup_dir2
   
    if (x3>=x2) and (y3>=y2) or (x1<=x4) and (y1<=y4):
        return True
    else:
        return Fals
# segunda etapa - calculo do resultado