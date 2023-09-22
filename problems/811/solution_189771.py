def colchao(medidas, H, L):
    '''Esta funcao diz se um colchao passa ou nao pelas portas de uma casa, dadas as dimensoes das portas e do colchao.'''
    '''list --> bool'''
    if medidas[1] <= H:
        return True
    elif (medidas[1] + medidas[2]) < (H + L):
        return True
    else:
        return False