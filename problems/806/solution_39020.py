#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos 1,y1,x2,y2 e x3 ,y3,x4,y4 do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    [x1,y1,x2,y2]= ret1
    [x3 ,y3,x4,y4  ] = ret2
    if ret1[x2] < ret2[x3] or ret2[x4] < ret1[x1] or ret1[y2] < ret2[y3] or ret2[y4]< ret1[y1]:
        return False