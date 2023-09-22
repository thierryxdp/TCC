#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2
    p1x=x_inf_esq1
    p2x=x_sup_dir1
    p3x=x_inf_esq2
    p4x=x_sup_dir2
    p1y=y_inf_esq1
    p2y=y_sup_dir1
    p3y=y_inf_esq2
    p4y=y_sup_dir2
    if (p1x<=p3x<=p2x)or(p1x<=p4x<=p4x) or (p3y<=p1x<=p4y) or (p3y<=p2y<=p4y) or (p3x<=p1x<=p4x) or (p3x<=p2x<=p4x) or (p1y<=p3y<=p2y) or (p1y<=p4y<=p2y):
        return True
    if not (p1x<=p3x<=p2x)or(p1x<=p4x<=p4x) or ((p3y<=p1x<=p4y) or (p3y<=p2y<=p4y) or (p3x<=p1x<=p4x) or (p3x<=p2x<=p4x) or (p1y<=p3y<=p2y) or (p1y<=p4y<=p2y):
        return False