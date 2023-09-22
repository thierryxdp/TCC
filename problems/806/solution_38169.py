#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos


# segunda etapa - calculo do def colisao(ret1,ret2):
    rect1_x = ret1[:1]
    rect1_y = ret1[2:3]
    rect1_width = ret1[4:5]
    rect1_height = ret1[6:7]

    rect2_x = ret2[:1]
    rect2_y = ret2[2:3]
    rect2_width = ret2[4:5]
    rect2_height = ret2[6:7]

    if (rect1_x < rect2_x + rect2_width and
            rect1_x + rect1_width > rect2_x and
            rect1_y < rect2_y + rect2_height and
            rect1_y + rect1_height > rect2_y):

        return True

    else:

        return False