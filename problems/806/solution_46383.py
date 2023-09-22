#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
	ret1[0]=xe1
    ret1[1]=ye2
    ret1[2]=xd1
    ret1[3]=yd1
    ret2[0]=xe2
    ret2[1]=ye2
    ret2[2]=xd2
    red2[3]=yd2
    if not(xd2<xe1 or xd1<xe2) and not(yd2<ye1 or yd1<ye2):
    return True
# segunda etapa - calculo do resultado