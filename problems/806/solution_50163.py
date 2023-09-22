#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    xie1 = ret1[0]
    yie1 = ret1[1]
    xsd1 = ret1[2]
    ysd1= ret1[3]
    xiq2 = ret2[0]
    yie2 = ret2[1]
    xsd2 = [2]
    ysd2 = [3]
# segunda etapa - calculo do resultado
	if int(max(xie1,xsd1)) < int(min(xiq2,xsd2)) or int(max(xiq2,xsd2)) < int(min(xie1,xsd1)) or int(max(yie1,ysd1)) < int(min(yie2,ysd2)) or int(max(yie2,ysd2)) < int(min(yie1,ysd1)):
        return False
    else:
        return True