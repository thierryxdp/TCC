def colisao(a,b):
    '''Retorna se os retângulos a e b tem colisão no plano cartesiano
tuple, tuple -> bool'''
    if (a[2]<b[0]) or (b[2]<a[0]) or (a[3]<b[1]) or (b[3]<a[1]):
        return False
    else:
        return True