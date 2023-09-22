def colchao(medidas, H, L):
    '''Função que verifica se o colchão passa ou não pelas portas, dadas
    as dimensões A, B e C do colchão e H e L da porta
    list, int, int -> bool'''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if B <= H:
        return True
    if B <= L:
        return True
    else:
        return False