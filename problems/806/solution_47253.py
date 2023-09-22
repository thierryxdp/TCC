def colisao(a,b):
    '''a funcao colisao recebe duas tuplas com quatro 
valores inteiros cada uma, representando as coordenadas
dos vertices inferior esquerdo e superior esquerdo do 
primeiro retângulo e do segundo retângulo, nessa ordem,
e devolve True se ha colisao entre os 2 retangulos e 
False, caso contrario.
    tuple, tuple --> bool'''

    a = x0, yo, x1, y1
    b = x2, y2, x3, y3
    
    bol = False
    if b[1] <= a[3] and b[1] >= a[1]:
        if b[0] <= a[2] and b[0] >= a[0]:
            bol = True
    elif b[3] >= a[1] and b[3] <= a[3]:
        if b[0] <= a[2] and b[0] >= a[0]:
            bol = True