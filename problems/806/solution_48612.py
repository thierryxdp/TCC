def colisao(ret1, ret2):
    '''A Função colisão recebe duas (2) tuplas com quatro valores inteiros
    coordenadas dos vertices inferior esquerdo e superior esquerdo do
    retangulo, nessa ordem, e devolve True se ha colisao entre as duas.
    tuple, tuples'''
   
    
    if ret1[0] == ret2[0]:
        return True
    if ret1[1] == ret2[1]:
        return True
    if ret1[2] == ret2[2]:
        return True
    if ret1[3] == ret2[3]:
        return True
    else :
        return False