def colisao(ret1,ret2):
    '''
    Detecta se há colisão entre doi retângulos.
    tuple, tuple --> bool
    '''
    v1_ret1=(ret1[2],ret1[1])
    v2_ret1=(ret1[2],ret1[3])
    v3_ret1=(ret1[0],ret1[1])
    v4_ret1=(ret1[0],ret1[3])
    v1_ret2=(ret2[2],ret2[1])
    v2_ret2=(ret2[2],ret2[3])
    v3_ret2=(ret2[0],ret2[1])
    v4_ret2=(ret2[0],ret2[3])
    if (ret1[3]>=ret2[1] and ret1[3]<=ret2[3]) or (ret2[3]>=ret1[1] and ret2[3]<=ret1[3]:
        return True
    elif (ret1[0]>=ret2[0] and ret1[0]<=ret2[2]) or (ret2[0]>=ret1[0] and ret2[0]<=ret1[2]:
        return True
    else:
        return False