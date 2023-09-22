#Start your python function here
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    a1=ret1[0]
    a2=ret1[1]
    a3=ret1[2]
    a4=ret1[3]
    b1=ret2[0]
    b2=ret2[1]
    b3=ret2[2]
    b4=ret2[3]
    if a2 == b1:
        return False
    if a1 == b1:
        return True
    if b3 >= a3 and b4 >= a4:
        return True
    if a1 < a4 and a2 < a3:
        return False
    if a1 != b1 and a2 != b2 and a3 != b3 and a4 != b4:
        return False
    
    
   
    
    
    
    

# segunda etapa - calculo do resultado