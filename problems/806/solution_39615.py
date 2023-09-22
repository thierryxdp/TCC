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

    pontoInfEsq1 = (x_inf_esq1, y_inf_esq1)
    pontoSupEsq1 = (x_inf_esq1, y_sup_dir1)
    pontoInfDir1 = (x_sup_dir1, y_inf_esq1)
    pontoSupDir1 = (x_sup_dir1, y_sup_dir1)
    
    pontoInfEsq2 = (x_inf_esq2, y_inf_esq2)
    pontoSupEsq2 = (x_inf_esq2, y_sup_dir2)
    pontoInfDir2 = (x_sup_dir2, y_inf_esq2)
    pontoSupDir2 = (x_sup_dir2, y_sup_dir2)

    condicao1 = False
    condicao2 = False
    
    if pontoInfEsq2[0] <= pontoInfEsq1[0] and pontoSupEsq2[0] <= pontoSupDir1[0] or pontoInfEsq2[0] >= pontoInfEsq1[0] and pontoSupDir2[0] >= pontoSupDir1[0]:
        condicao1 = True

    if pontoInfEsq2[1] >= pontoInfEsq1[1] and pontoSupEsq2[1] >= pontoSupDir1[1] or pontoInfEsq2[1] <= pontoInfEsq1[1] and pontoSupDir2[0] <= pontoSupDir1[1]:
        condicao2 = True
    
    if (pontoInfEsq2[0] <= pontoInfEsq1[0] and pontoInfEsq2[1] >= pontoInfEsq1[1]) and (pontoSupEsq2[0] <= pontoSupDir1[0] and pontoSupEsq2[1] >= pontoSupDir1[1]) or (pontoInfEsq2[0] >= pontoInfEsq1[0] and pontoInfEsq2[1] <= pontoInfEsq1[1]) and (pontoSupDir2[0] >= pontoSupDir1[0] and pontoSupDir2[0] <= pontoSupDir1[1]):
        condicao2 = True

    return condicao1 and not condicao2 or condicao2 and not condicao1 or not condicao1 and not condicao2