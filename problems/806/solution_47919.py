#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

    xa, ya, xb, yb = ret1
    x1, y1,  x3, y3 = ret2
    xc = xa
    yc = yb
    xd = xb
    yd = ya
    x2 = x1
    y2 = y3
    x4 = x3
    y4 = y1
    if xa<=x1<=xb and ya<=y1<=yb or xa<=x2<=xb and ya<=y2<=yb or xa<=x3<=xb and ya<=y3<=yb or xa<=x4<=xb and ya<=y4<=yb or x1<=xa<=x3 and y1<=ya<=y3 or x1<=xb<=x3 and y1<=yb<=y3 or x1<=xc<=x3 and y1<=yc<=y3 or x1<=xd<=x3 and y1<=yd<=y3:
        return True
    else:
        return False