#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    rect1_x=ret1[:1]
    rect1_y=ret1[2:3]
    rect1_width=ret1[4:5]
    rect1_height=ret1[6:7]
    rect2_x=ret2[:1]
    rect2_y=ret2[2:3]
    rect2_width=ret2[4:5]
    rect2_height=ret2[6:7]
    if (rect2_x<=rect1_x+rect1_width)and(rect2_x+rect2_width>rect1_x)and(rect2_y<=rect1_y+rect1_heigth)and(rect2_y+rect2_width>=rect1_y):
        return True