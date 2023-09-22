#Start your python function here
import math
def dist(a, b, c, d):
    """Retorna a distância entre os pontos A e B"""
    A = (a,b)
    B = (x,y)
    return math.sqrt((x-a)**2+(y-b)**2)
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    a, b, c, d = ret1
    x, y, z, w = ret2
	A = (a, b)
    B = (c, d)
    C = (x, y)
    D = (z, w)
    string = ''
# segunda etapa - calculo do resultado
	if dist(a,b,x,y) == 0:
        string += 'True'
    if dist(c,d,z,w) == 0:
        string += 'True'
    if dist(a,b,z,w) == 0:
        string += 'True'
    if dist(c,d,x,y) == 0:
        string += 'True'
    return string