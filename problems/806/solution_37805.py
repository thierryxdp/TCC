#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

# primeira etapa - extrair as coordenadas das tuplas recebidas como argumentos
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    a=ret1[0]
    b=ret1[1]
    c=ret1[2]
    d=ret1[3]
    x=ret2[0]
    y=ret2[1]
    z=ret2[2]
    w=ret2[3]
    if a==x:
        return True
    elif b==y:
        return True
    elif d==w:
        return True
    elif b==x:
        return False
    elif z>c:
        return True
    elif w<d:
        return False
     elif c==z:
        return True
    else:
        return False

# segunda etapa - calculo do resultado