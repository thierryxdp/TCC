def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

(x,y,x1,y1) (x,y,x1,y1)
    xie1, yie1, xsd1, ysd1 = ret1
    xie2, yie2, xsd2, ysd2 = ret2
    return not(xsd1<xie2 or xsd2<xie1 or ysd1<yie2 or ysd2<yie1)