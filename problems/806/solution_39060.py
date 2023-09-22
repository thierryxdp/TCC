#Start your python function here
def colisao(a,b):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
	r1x=(a[0],a[2])
    r1y=(a[1],a[3])
    r2x=(b[0],b[2])
    r2y=(b[1],b[3])
    if max(r1x)<=max(r2x):
        return max(r1x)>=min(r2x)
    elif max(r1y)<=max(r2y):
        return max(r1y)>=min(r2y)
    elif max(r2x)<max(r1x):
        return max(r2x)>=min(r1x)
    else:
        return max(r2y)>min(r1y)