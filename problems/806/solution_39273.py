#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
   x = [[0,0],[0,0]]
y = [[0,0],[0,0]]
# crie uma matriz
# em python uma matriz são listas dentros de listas

x[0][0], y[0][0], x[0][1], y[0][1] = input().split(" ", 3)
x[1][0], y[1][0], x[1][1], y[1][1] = input().split(" ", 3)
# usei o split() para poder a cada espaço ele atribuir o numero a
# uma variavel diferente(no caso um espaço diferente da matriz)
# o numero dentro do split é para indicar quantas vezes ele vai separar
# usei 3 pois ele conta o 0, então 0,1,2,3 são 4 numeros
#for i in range(0, 2):
	for j in range(0, 2):
		x[i][j] = int(x[i][j])

for i in range(0, 2):
	for j in range(0, 2):
		y[i][j] = int(y[i][j])
if (x[0][1] < x[1][0]) or (x[1][1] < x[0][0]) or (y[0][1] < y[1][0]) or (y[1][1]  x[1][1]) or (x[1][0] > x[0][1]) or (y[0][0] > y[1][1]) or (y[1][0] > y[0][1]):
	print(0)
else:
	print(1)
# segunda etapa - calculo do resultado