#Start your python function here
def colisao(a,b):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = a
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = b

# segunda etapa - calculo do resultado
	x1=a[0]
    y1=a[1]
    x2=a[2]
    y2=a[3]
    x3=b[0]
    y3=b[1]
    x4=b[2]
    y4=b[3]
    if not (x4<x1 or x2<x3)and not(y4<y1 or y2<y3):
        return True
    else:
        return False