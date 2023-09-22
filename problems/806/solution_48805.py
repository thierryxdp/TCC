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
    
    if x2<x3:
        return False
    
    if x4<x1:
        return False
    
    if y2<y3:
        return False
    
    if y4<y1:
        return False