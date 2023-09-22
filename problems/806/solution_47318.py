def colisao(ret1,ret2):
    '''Funcao que recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos 4 vertices e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

    #ret1 e ret2 = tuple()
    #x1, y1, x2, y2 = ret1
    #x3, y3, x4, y4 = ret2

# segunda etapa - calculo do resultado

    if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        return True

    else:
        return False