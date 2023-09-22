#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

ret1 = (x1,y1,x2,y2,)
ret2 = (x3,y3,x4,y4,)
# segunda etapa - calculo do resultado
x1=ret1[0]
y1=ret1[1]
x2=ret1[2]
y2=ret1[3]
x3=ret2[0]
y3=ret2[1]
x4=ret2[2]
y4=ret2[3]

if x2<x3 or x4<x1 or y2<y3 or y4<y1:
    False
else:
    True