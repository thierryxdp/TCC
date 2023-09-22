#Start your python function here
'''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
x[0] [0], y[0] [0], x[0] [1], y[0] [1] = ret1
x[1] [0], y[1] [0], x[1] [1], y[1] [1]= ret2
def colisao(ret1,ret2):
   if (x[0] [1]<x[1] [0]) or (x[1] [1]<x[0] [0]) or (y[0] [1]<y[1] [0]:
      return(0)
  else:
       return(1)