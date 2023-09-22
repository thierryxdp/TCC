def colisao(ret1: tuple, ret2: tuple) -> bool:
    """Verifica se há colisão entre os retângulos representados pelas
       coordenadas

       Parameters:
       ret1: Primeira tupla, representando as coordenadas dos dois vértices
       do primeiro retângulo
       ret2: Segunda tuplas, representando as coordenadas dos dois vértices
       do segundo retângulo

       Return:
       Se há colisão (sobreposição) entre os retângulos 1 e 2 no plano 2D

       Examples:
       colisao((0, 0, 1, 1), (0, 0, 1, 1)) == True
       colisao((0, 0, 2, 2), (1, 1, 3, 3)) == True
       colisao((0, 0, 1, 1), (2, 2, 3, 3)) == False
    """

    r1x1 = ret1[0]
    r1y1 = ret1[1]
    r1x2 = ret1[2]
    r1y2 = ret1[3]
    r2x1 = ret2[0]
    r2y1 = ret2[1]
    r2x2 = ret2[2]
    r2y2 = ret2[3]
    
    return (((r2x1 > r1x2) and (r2y1 > r1y2))
    or ((r1x1 > r2x2) and (r1y1 > r2y2))
    or ((r1x1 > r2x1) and (r1y1 > r2y2))
    or ((r2x1 > r1x2) and (r2y1 > r1y1))) == False