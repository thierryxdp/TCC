def colchao (medidas, H,L):
    '''
    essa função determina se o colchao passará pelas portas dado as suas medidas e a altura e largura das portas
    '''
    if (medidas == H*L) or (medidas[1] < H) or (medidas[2] < L):
        return True
    else:
        return False