def pontos(ret):
    xv1, yv1, xv2, yv2 = ret
    lista = []
    
    for x in (xv1, xv2):
        for y in (yv1, yv2):
            lista.append((x, y))
    
    return lista    
    

#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

	return pontos(ret1)