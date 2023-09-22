def colisao(ret1,ret2):
    '''função que determina se dois retângulos se interceptam
    ou não. recebe duas tuplas com quatro valores inteiros cada uma,
    representando as coordenadas dos vértices inferior esquerdo
    e superior esquerdo do primeiro retângulo e do segundo 
    retângulo, nessa ordem. devolve True se há colisao entre 
    os 2 retangulos e False, se não
    tupla tupla -> bool'''
    ret1 = x1,y1,x2,y2
    ret2 = x3,y3,x4,y4
    
    if x1<=x3:
        return True
    
    if x2<=x4:
        return True
    
    if y2<=y4:
        return True
    
    if y1<=y3:
        return True
    
    else:
        return False