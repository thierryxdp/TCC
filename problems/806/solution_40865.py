#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    xla,yla, x2a,y2a = ret1
    xlb,ylb, x2b,y2b = ret2
    if x2b < xla or x2a < xlb:
        xok = True
    else:
        xok = False
    if y2b < yla or y2a < ylb:
        yok = True
    else:
        yok= False
    if xok or yok:
        return False
    else: 
        return True