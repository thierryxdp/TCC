def colisao(C1, C2):
    '''Retorna se dois retângulos colidem, dadas as coordenadas da sua diagonal.
       tuple(float, float),tuple(float, float) -> bool'''
    return not (C2[2] < C1[0] or C1[2] < C2[0]) and not (C2[2] < C1[1] or C1[2] < C2[1])