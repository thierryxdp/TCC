def colchao (medidas, H,L):
    ''' funçao que dados os parametros caclula a medida de um colchao e retorna se ele passa em uma porta'''
    '''list, int->bool'''
    
    medidas.sort()
    
    altura=medidas[0]
    largura=medidas[1]
    comprimento=medidas[2]
    
    if comprimento < H:
        return True
    if largura < H:
        return True
    if largura L:
        return True
     
    return False