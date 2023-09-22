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
def calculo_colisao (tupla1,tupla2):
    if tupla2[0]>= tupla1[0] and tupla2[0] <= tupla1[2]:
        if tupla2[1] >= tupla1[1] and tupla2[1] <= tupla1[3]:
            return ("True")
    elif tupla2[2]>= tupla1[0] and tupla2[2] <= tupla1[2]:
            if tupla2[3] >= tupla1[1] and tupla2[3] <= tupla1[3]:
                return ("True")
    elif tupla2[0]>= tupla1[0] and tupla2[0] <= tupla1[2]:
            if tupla2[3] >= tupla1[1] and tupla2[3] <= tupla1[3]:
                return ("True")
    elif tupla2[2]>= tupla1[0] and tupla2[2] <= tupla1[2]:
            if tupla2[1] >= tupla1[1] and tupla2[1] <= tupla1[3]:
                return ("True")
    else:
        return ("False")