def colchao(medidas, H, L):
    '''Dadas as medidas de altura, largura e comprimento de um colchão,
    calcula se esse colchão passaria em uma porta com altura = H 
    e largura = L dadas como parâmetro também.'''
    
    if medidas[0] <= H and medidas [0] <= L:
        return True
    else: 
        return False