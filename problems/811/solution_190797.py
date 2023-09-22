def colchao(medidas, H, L):
    '''Retorna se o Colchão passa pela porta, dada as medidas do colchão;
    list, float, float=> bool'''
    
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