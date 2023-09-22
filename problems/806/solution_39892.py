#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    def colisao(r1,r2):
    x1=r1[0]
    y1=r1[1]
    x2=r1[2]
    y2=r1[3]
    x3=r1[0]
    y3=r2[1]
    x4=r2[2]
    y4=r2[3]
    if x<2<x3 or x4<x1 or y2<y3 or y4<y1:
        return False
    else:
        return True