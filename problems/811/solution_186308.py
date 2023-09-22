def colchao (medidas, h, l):
    """função que retorna true se o colchao tem capacidade de passar
    na porta, ou false se o colchao nao passa pela porta"""
    larg = medidas[1]
    alt = medidas[2]
    if larg < l and alt < h:
        return True
    if larg < l and alt > h:
        return True
    if larg > l and alt < h:
        return True
    if larg < h
    return True
    else:
        return False