def colchao(medidas, H, L):
    '''Função que verifica se o colchão passa ou não pelas portas, dadas
    as dimensões A, B e C do colchão e H e L da porta
    list, int, int -> bool'''
    A = medidas[0]
    B = medidas[1]
    x = (A*math.sqrt(2))/2
    y = A*(L - x)/B
    if B <= H:
        return True
    elif B**2 <= (L - x)**2 + (H - y)**2:
        return True
    else:
        return False