def colchao(medidas,H,L):
    '''Retornar se as condições são verdadeiras ou falsas
    list,int,int-> bool'''
    
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False