def colisao(ret1, ret2):
    """ A função retorna True se há colisão entre dois
    retângulos em um plano e False, se não ocorrer
    essa colisão.
    Tuple, tuple -> bool """
    
    p1x = ret1[0]
    p1y = ret1[1]
    p2x = ret1[2]
    p2y = ret1[3]

    p3x = ret2[0]
    p3y = ret2[1]
    p4x = ret2[2]
    p4y = ret2[3]

    if p1x <= p3x <= p2x and p1y <= p3y <= p2y:
        return True
    if p1x <= p4x <= p2x and p1y <= p4y <= p2y:
        return True
    if p3x <= p1x <= p4x and p3y <= p1y <= p4y:
        return True
    if p3x <= p2x <= p4x and p3y <= p2y <= p4y:
        return True
    else:
        return False