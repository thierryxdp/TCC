#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultadox1= ret_1 pont_esq
    x1= x_sup_dir1
    y1= y_sup_dir1
    x2= x_inf_esq1
    y2= y_inf_esq1
    x3= x_sup_dir2
    y3= y_sup_dir2
    x4= x_inf_esq2
    y4= y_inf_esq2
    elif y4<y2 and y1<y3 and x1<x3 and x2<x4:
        return 'true'
    elif y1>y3 and y4<y2 and x1<x3 and x2<x4:
        return 'true'
    elif y1<y3 and y4<y2 and x1<x3 and x2<x4:
        return 'true'
    elif y1=y3 and y2=y4 and x1<x3 and x2<x4:
        return 'true'
    elif y1>y3 and y2>y4 and x1=x3 and x2=x4:
        return 'true'
    elif y1=y3 and y2=y4 and x1=x3 and x2=x4:
        return 'true'
    else:
        return 'False'