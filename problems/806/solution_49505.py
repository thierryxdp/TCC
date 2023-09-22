#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
	x1_1= retangulo_1[0]
    y1_1= retangulo_1[1]
    x2_1= retangulo_1[2]
    y2_1= retangulo_1[3]
    x1_2= retangulo_2[0]
    y1_2= retangulo_2[1]
    x2_2= retangulo_2[2]
    y2_2= retangulo_2[3]
    resposta= ()
    if (x1_1<=x1_2<=x2_1 or x1_1<=x2_2<=x2_1 or x1_2<=x1_1<=x2_2 or x1_2<=x2_1<=x2_2) and (y1_1<=y1_2<=y2_1 or y1_1<=y2_2<=y2_1 or y1_2<=y1_1<=y2_2 or y1_2<=y2_1<=y2_2):
        return True
    else:
        return False