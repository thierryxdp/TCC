def colchao (medidas, H, L):
    '''retorna um valor booleano para o calculo das medidas do colchao e o vao da porta'''
    '''list, int, int -> bool'''
    if medidas [1] <= H:
        return True
    if medidas [1] <= L:
        return True
    else:
        return False