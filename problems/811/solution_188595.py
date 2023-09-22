def colchao(medidas, h, l):
    """Função que verifica se o colchão é maior do que a porta"""
    """list, float, float -> bool"""
    if medidas[1] > h and medidas[2] > l:
        return False
    else:
        return True