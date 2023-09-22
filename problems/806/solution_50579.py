def pontos (ret):
    xv1,yv1,xv2,yv2 = ret
    return [(x,y) for x in range (xv1, xv2 +1) for y in range (yv1, yv2 +1)]
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.'''
	a1 = pontos (ret1)
    a2 = pontos (ret2)
    
    test = False
    for p in al:
        if(p in a2):
            test = True
         break
         return test