#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2

# segunda etapa - calculo do resultado
a = ret1[0:2]
b = ret2[2:]
c = ret1[2:]
d = ret2[0:2] 
if a[0:1] and a[1:2] == b[0:1] and b[1:2] or c[0:1] and c[1:2] == d:
     True
elif a[0:1] and a[1:2] == d[0:1] and d[1:2] or b[0:1] and b[1:2] == c[0:1] and c[1:2]:
    return True
if d[0:1] and d[1:2] > a[0:1] and a[1:2] > b[0:1] and b[1:2]:
    return True
elif a[0:1] and a[1:2] > d[0:1] and d[1:2] > c[0:1] and c[1:2]:
    return True
if d[0:1] and d[1:2] > c[0:1] and c[1:2] > b[0:1] and b[1:2]:
    return True
elif a[0:1] and a[1:2] > b[0:1] and b[1:2] > c[0:1] and c[1:2]:
    return True
else:
    return False