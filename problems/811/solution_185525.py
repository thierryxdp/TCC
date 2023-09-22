def colchao(medidas, H, L):
    '''funçao que dados os parametros calcula as medidas de um colchao e se ele passara em uma porta'''
    '''list, str->bool'''
    medidas.sort()
    
    altura=medidas[0]
    largura=medidas[1]
    comprimento=[2]
    
    if comprimento  < H:
        return True
    if largura < H:
        return True
    if largura < L:
        return True
    else:
        return False