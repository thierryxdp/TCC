def colchao(medidas,h,l):
    '''Essa função recebe uma lista com as medidas de um colchão
    e dois números correspondentes às dimensões da porta da casa, assim calcula se um determinado
    colchão comprado poderá ou não passar pela porta;
    LIST, FLOAT, FLOAT -> BOOL'''
    ccolc = max(medidas[0],medidas[1],medidas[2])
    gcolc = min(medidas[0],medidas[1],medidas[2])
    lcolc = (medidas[0]+medidas[1]+medidas[2])-(ccolc+gcolc)
    if (lcolc <= h and gcolc < l):
        return True
    else:
        return False