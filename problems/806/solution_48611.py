def colisao(ret1, ret2):
    '''A Função colisão recebe duas (2) tuplas com quatro valores inteiros
    coordenadas dos vertices inferior esquerdo e superior esquerdo do
    retangulo, nessa ordem, e devolve True se ha colisao entre as duas.
    tuple, tuples'''
    ret1 =sum(ret1)
    ret2 =sum(ret2)
    
    if ret1 != ret2:
        return True
    else :
        return False