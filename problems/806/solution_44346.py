#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x1, y1, x1, y1 = ret1
    a1, b1,  a2, b2 = ret2

# segunda etapa - calculo do resultado
x1=ret1[0]
y1=ret1[1]
x2=ret1[2]
y2=ret1[3]
a1=ret2[0]
b1=ret2[1]
a2=ret2[2]
b2=ret2[3]
if a1<=x1 and x1<=b2 and b1<=y1 and y1<=b2:
    return 'true'
elif a1<=x2 and x2<=b2 and b1<=y2 and y2<=b2:
    return 'true'
elif  x1<=a1 and a1<=x2 and y1<=b1 and b1<=y2:
    return 'true'
elif  x1<=a2 and a2<=x2 and y1<=b2 and b2<=y2:
    return 'true'
else:
    return 'false'