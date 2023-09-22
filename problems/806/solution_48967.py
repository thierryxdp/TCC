#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

for i in range (0,2):
    for j in range (0,2):
        x[i][j] = int (x[i][j])
        
for i in range(0,2):
    for j in range (0,2):
        y[i][j] = int (y[i][j])
if x[0][1] < x[1][0]) or (x[1][1] < x[0][0]) or (y[0][1] < y[1][0]) or (y[1][1]  x[1][1]) or (x[1][0] > x[0][1]) or (y[0][0] > y[1][1]) or (y[1][0] > y[0][1]):
	return(0)
else:
	return(1)