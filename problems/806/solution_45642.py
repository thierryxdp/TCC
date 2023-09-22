#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada
     uma, representando as coordenadas dos vertices inferior esquerdo e
     superior esquerdo do primeiro retângulo e do segundo retângulo,
     nessa ordem, e devolve True se ha colisao entre os 2 retangulos e
     False, caso contrario. tuple, tuple --> bool'''
    
# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    
    xi1=x_inf_esq1
    yi1=y_inf_esq1
    xs1=x_sup_dir1
    ys1=y_sup_dir1
    xi2=x_inf_esq2
    yi2=y_inf_esq2
    xs2=x_sup_dir2
    ys2=y_sup_dir2

#os 4 vértices dos retângulos
    retan1=(xi1,yi1),(xs1,yi1),(xi1,ys1),(xs1,ys1)
    retan2=(xi2,yi2),(xs2,yi2),(xi2,ys2),(xs2,ys2)

# segunda etapa - calculo do resultado
    if retan1 or retan2:
        return True
    else:
        return False