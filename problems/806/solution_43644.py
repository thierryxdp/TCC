#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
  
    if (x[0][1] < x[1][0] || x[1][1] < x[0][0] || y[0][1] < y[1][0] || y[1][1] < y[0][0] || x[0][0] > x[1][1] || x[1][0] > x[0][1] || y[0][0] > y[1][1] || y[1][0] > y[0][1]):
         return(0)