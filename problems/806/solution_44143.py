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
def colisao(tup1,tup2):
    """dados dois retângulos, em que cada retângulo é determinado pelas coordenadas x e y
    de dois de seus vértices  diametralmente opostos, representando a diagonal que vai da esquerda
    para a direita e de baixo para cima, a função retorna se eles se interceptam ou não em formato
    booleano;
    tup,tup->bool"""
    Ax=tup1[0]
    Ay=tup1[1]
    Bx=tup1[2]
    By=tup1[3]
    Cx=tup2[0]
    Cy=tup2[1]
    Dx=tup2[2]
    Dy=tup2[3]
    if (Bx>Cx and Dx>Ax) and (By>Cy and Cy>Ay):
        return True
    else:
        return False