def colisao (t1, t2):
    '''função que dadas duas tuplas (t1 e t2) com quatro valores inteiros cada
    uma, representando as coordenadas do primeiro retângulo e do segundo
    retângulo, retorna True caso haja colisão ou False, caso não haja;
    tuple(int,int,int,int), tuple(int,int,int,int) -> bool'''
    if not (t2[2] < t1[0] or t1[2] < t2[0]) and not (t2[3] < t1[1] or t1[3] < t2[1]):
        return True
    else:
        return False