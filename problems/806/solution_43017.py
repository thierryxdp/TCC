def colisao(tup1,tup2):
    '''Duas tuplas, cada uma com suas coordenadas. 
       Devolve 'True" se há colisão e 'False' caso contrario.
       tuple, tuple --> bool'''
    if tup1[2] < tup2[0] or tup1[0] > tup2[2] or tup1[3] < tup2[1] or tup1[1] < tup2[3}]:
        return False
    else:
        return True