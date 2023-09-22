#-------EXERCICIO 7--------------

def colisao(ret1,ret2):
    
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''


    xie1 = ret1[0]
    yie1 = ret1[1]
    xsd1 = ret1[2]
    ysd1 = ret1[3]

    xie2 = ret2[0]
    yie2 = ret2[1]
    xsd2 = ret2[2]
    ysd2 = ret2[3]

    return not (xsd2 < xie1 or xsd1 < xie2) and not (ysd2 < yie1 or ysd1 < yie2)