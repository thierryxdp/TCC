def intercala(L1, L2):
    '''dado duas listas(L1,L2) calcula uma terceira(L3) que intercala os elementos das duas listas de entrada'''
    ''' lista,lista->lista'''
    L3=L1[0:1]+L2[0:1]+L1[1:2]+L2[1:2]+L1[-2:]+L2[-2:]
    return L3