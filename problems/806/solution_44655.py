def colisao(ret1,ret2):
    ret1 = (x1,y1,x2,y2)
    ret2 = (x3,y3,x4,y4)
    if x2<x3:
        if x4<x1:
            if y2<y3:
                if y4<y1:
                    return "False"
                else:
                    return "True"

    
    
'''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
tuple, tuple --> bool'''