def colchao(medidas, H, L):
    '''Função que verifica se o colchão passa ou não pelas portas, dadas
    as dimensões A, B e C do colchão e H e L da porta
    list, int, int -> bool'''
    A = medidas[0]
    B = medidas[1]
    if A**2 + B**2 <= H**2 + L**2:
        return True
    else:
        return False