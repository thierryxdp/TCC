def ver_tam([A, B, C], H, L):
    '''Função que verifica se o colchão passa ou não pelas portas, dadas
    as dimensões A, B e C do colchão e H e L da porta
    list, int, int -> bool'''
    if B <= H:
        return True
    else:
        return False