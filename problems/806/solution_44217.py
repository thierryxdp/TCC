#Start your python function here
def colisao(x,y):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

x = [[0,0],[0,0]]
y = [[0,0],[0,0]]

for i in range(0, 2):
	for j in range(0, 2):
		x[i][j] = int(x[i][j])

for i in range(0, 2):
	for j in range(0, 2):
		y[i][j] = int(y[i][j])

if (x[i][j] < x[i][j]) or (x[i][j] < x[i][j]) or (y[i][j] < y[i][j]) or (x[i][j] > x[i][j]) or (y[i][j] > y[i][j]) or (y[i][j] > y[i][j]):
	bool(False) 
else:
	bool(True)