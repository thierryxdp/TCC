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
    if v1_ret1==v1_ret2 or v1_ret1==v2_ret2 or v1_ret1==v3_ret2 or v1_ret1==v4_ret2:
        return True
    elif v2_ret1==v1_ret2 or v2_ret1==v2_ret2 or v2_ret1==v3_ret2 or v2_ret1==v4_ret2:
        return True
    elif v3_ret1==v1_ret2 or v3_ret1==v2_ret2 or v3_ret1==v3_ret2 or v3_ret1==v4_ret2:
        return True
    elif v4_ret1==v1_ret2 or v4_ret1==v2_ret2 or v4_ret1==v3_ret2 or v4_ret1==v4_ret2:
        return True
    elif 
    else:
        return False