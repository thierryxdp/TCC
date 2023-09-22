#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    xie1, yie1, xsd1, ysd1 = ret1
    xie2, yie2,  xsd2, ysd2 = ret2
    xie1 ==xsd2 and yie1==ysd2 or xsd1==xie2 and ysd2==yie2