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
if a = b or c = d:
    return True
elif a == d or b == c:
    return True
if d > a > b:
    return True
elif a > d > c:
    return True
if d > c > b:
    return True
elif a > b > c:
    return True
else:
    return False