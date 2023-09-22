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
    x2,y2=x_sup_dir1,y_sup_dir1
    x3,y3=x_inf_esq2,y_inf_esq2
    x4,y4=x_sup_dir2,y_sup_dir2
# segunda etapa - calculo do resultado
    if ( x3<= x2 ) or ( x1<= x4 ) and ( y3<= y2 ) or ( y1<= y4 ):
        return True
    else:
        return False