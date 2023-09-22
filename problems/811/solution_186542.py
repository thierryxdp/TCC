def colchao(medidas, H, L):
    '''Função que verifica se o colchão passa ou não pelas portas, dadas
    as dimensões A, B e C do colchão e H e L da porta
    list, int, int -> bool'''
    import math
    A = medidas[0]
    B = medidas[1]
    x = (A*math.sqrt(2))/2
    if B <= H:
        return True
    elif B <= ((L - x)**2 + (H - x)**2):
        return True
    else:
        return False