#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    ret1 = a1, a2, a3, a4
    ret2 = b1, b2, b3, b4
    if a1 == b1 or a2 == b2 or a3 == b3 or a4 == b4:
        return True
    
    

# segunda etapa - calculo do resultado