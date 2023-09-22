def colisao(ret1,ret2):
    '''Dado duas tuplas com quatro valores inteiros (que representa
    a coordenadas dos vértices inferior esquerdo e superior direito
    do primeiro e segundo retângulo, respectivamente), a funçao
    devolve True se houve colisão entre os 2 retângulos e False,
    caso não ocorra.
    Parametros de Entrada: tupla, tupla
    Retorna: booleana'''
    x1,y1,x2,y2=ret1[0],ret1[1],ret1[2],ret1[3]
    x3,y3,x4,y4=ret2[0],ret2[1],ret2[2],ret2[3]
    
    if (x4<x1 or x2<x3 or y4<y1 or y2<y3):
        return False
    else:
        return True