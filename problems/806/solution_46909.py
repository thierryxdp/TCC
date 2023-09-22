def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

a=int(ret1[0])
b=int(ret1[1])
c=int(ret1[2])
d=int(ret1[3])
e=int(ret2[0])
f=int(ret2[1])
g=int(ret2[2])
h=int(ret2[3])
	if (a=<e=<c and b=<f=<d) or (a=<g=<c and b=<h=<d)