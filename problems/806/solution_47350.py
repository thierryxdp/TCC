#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores 
     inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior 
     esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao 
     entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

    ax1, ay1 = x_inf_esq1, y_inf_esq1
    ax2, ay2 = x_sup_dir1, y_inf_esq1
    ax3, ay3 = x_sup_dir1, y_sup_dir1
    ax4, ay4 = x_inf_esq1, y_sup_dir1

    bx1, by1 = x_inf_esq2, y_inf_esq2
    bx2, by2 = x_sup_dir2, y_inf_esq2
    bx3, by3 = x_sup_dir2, y_sup_dir2
    bx4, by4 = x_inf_esq2, y_sup_dir2
    
# segunda etapa - calculo do resultado